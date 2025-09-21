"""
Notion API client wrapper
"""

import re
from typing import Dict, Any, List, Tuple
from notion_client import Client
import logging

logger = logging.getLogger(__name__)


class NotionClient:
    """Wrapper for Notion API operations"""

    def __init__(self, token: str):
        """Initialize Notion client"""
        self.client = Client(auth=token)

    @staticmethod
    def extract_page_id(url_or_id: str) -> Tuple[str, str]:
        """
        Extract page ID from various Notion URL formats
        Returns tuple of (page_id, page_title_hint)
        """
        # If it's already just an ID (32 character hex string)
        if re.match(r'^[a-f0-9]{32}$', url_or_id.replace('-', '')):
            return url_or_id, ""

        # Extract from URL
        if "notion.so" in url_or_id or "notion.site" in url_or_id:
            # Remove query parameters
            url_without_params = url_or_id.split('?')[0]

            # Extract the last part of the URL path
            path_parts = url_without_params.split('/')
            last_part = path_parts[-1] if path_parts else ""

            # Try to extract title hint and ID
            title_hint = ""
            if '-' in last_part:
                parts = last_part.split('-')
                # The ID is typically the last 32-character hex string
                for i in range(len(parts) - 1, -1, -1):
                    potential_id = ''.join(parts[i:])
                    if len(potential_id) >= 32:
                        page_id = potential_id[:32]
                        title_hint = '-'.join(parts[:i])
                        return page_id, title_hint

            # Fallback: try to find any 32-character hex string
            hex_pattern = r'[a-f0-9]{32}'
            matches = re.findall(hex_pattern, last_part.replace('-', ''))
            if matches:
                return matches[0], ""

        return url_or_id, ""

    def fetch_page_content(self, page_id: str) -> Dict[str, Any]:
        """Fetch page content from Notion"""
        # Get page metadata
        page = self.client.pages.retrieve(page_id=page_id)

        # Get page blocks (content)
        blocks = []
        start_cursor = None

        while True:
            if start_cursor:
                response = self.client.blocks.children.list(
                    block_id=page_id,
                    start_cursor=start_cursor
                )
            else:
                response = self.client.blocks.children.list(block_id=page_id)

            blocks.extend(response['results'])

            if not response['has_more']:
                break
            start_cursor = response['next_cursor']

        return {
            'page': page,
            'blocks': blocks
        }

    def fetch_database_pages(self, database_id: str) -> List[Dict]:
        """Fetch all pages from a database"""
        response = self.client.databases.query(database_id=database_id)
        return response['results']

    def fetch_children_blocks(self, block_id: str) -> List[Dict]:
        """Fetch children blocks for a given block"""
        try:
            response = self.client.blocks.children.list(block_id=block_id)
            return response['results']
        except Exception as e:
            logger.warning(f"Could not fetch children for block {block_id}: {e}")
            return []

    @staticmethod
    def extract_text_from_rich_text(rich_text_array: List[Dict]) -> str:
        """Extract plain text from Notion rich text array"""
        text = ""
        for text_block in rich_text_array:
            if text_block['type'] == 'text':
                text += text_block['text']['content']
            elif text_block['type'] == 'mention':
                text += text_block['plain_text']
        return text

    @staticmethod
    def extract_title(page_data: Dict[str, Any]) -> str:
        """Extract title from page properties"""
        properties = page_data['page']['properties']

        for prop_name, prop_value in properties.items():
            if prop_value['type'] == 'title':
                if prop_value['title']:
                    return NotionClient.extract_text_from_rich_text(prop_value['title'])

        return "Untitled Document"