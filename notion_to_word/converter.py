"""
Main converter class for Notion to Word
"""

import os
import re
from datetime import datetime
from typing import Optional, List
import logging

from .config import TemplateConfig
from .notion_client import NotionClient
from .word_formatter import WordFormatter
from .block_processor import BlockProcessor

logger = logging.getLogger(__name__)


class NotionToWordConverter:
    """Main converter class that orchestrates the conversion process"""

    def __init__(self, notion_token: str, template_path: Optional[str] = None,
                 output_dir: str = "outputs", config_path: str = "template_config.json"):
        """
        Initialize the converter

        Args:
            notion_token: Notion API integration token
            template_path: Path to Word template file
            output_dir: Directory for output files
            config_path: Path to template configuration JSON
        """
        self.notion = NotionClient(notion_token)
        self.template_path = template_path
        self.output_dir = output_dir
        self.config_manager = TemplateConfig(config_path)

        # Determine template name based on path
        if template_path:
            template_basename = os.path.basename(template_path).lower()
            if "default" in template_basename:
                self.template_name = "default"
            else:
                self.template_name = "custom"
        else:
            self.template_name = "default"

        self.template_config = self.config_manager.get_template(self.template_name)
        self.formatter = WordFormatter(self.template_config)
        self.processor = BlockProcessor(self.notion, self.formatter, self.template_config)

        # Create output directory
        os.makedirs(self.output_dir, exist_ok=True)

    def convert_page(self, url_or_id: str, output_path: Optional[str] = None) -> str:
        """
        Convert a Notion page to a Word document

        Args:
            url_or_id: Notion page URL or ID
            output_path: Optional custom output path

        Returns:
            Path to the created Word document
        """
        # Extract page ID
        page_id, _ = NotionClient.extract_page_id(url_or_id)
        logger.info(f"Converting page ID: {page_id}")

        # Fetch content
        print(f"📄 Fetching page content...")
        content = self.notion.fetch_page_content(page_id)

        # Create document
        doc = self.formatter.create_document(self.template_path)

        # Add title
        title = NotionClient.extract_title(content)
        title_style = self.config_manager.get_style_for_block("title", self.template_name)
        self.formatter.add_title(doc, title, title_style)

        # Add metadata
        created_time = content['page'].get('created_time', '')
        last_edited = content['page'].get('last_edited_time', '')
        self.formatter.add_metadata(doc, created_time, last_edited)

        # Process blocks
        print(f"⚙️  Processing {len(content['blocks'])} blocks...")
        style_mappings = self.template_config.get("style_mappings", {})
        self.processor.process_blocks(content['blocks'], doc, style_mappings)

        # Generate output path
        if not output_path:
            output_path = self._generate_output_path(title)

        # Save document
        doc.save(output_path)
        print(f"✅ Document saved to: {output_path}")

        # Print statistics if there were any issues
        if self.processor.stats["blocks_with_errors"] > 0:
            print(f"\n📊 Statistics:")
            print(f"   Blocks processed: {self.processor.stats['blocks_processed']}")
            print(f"   Blocks with errors: {self.processor.stats['blocks_with_errors']}")

        return output_path

    def convert_database(self, database_url_or_id: str) -> List[str]:
        """
        Convert all pages in a Notion database

        Args:
            database_url_or_id: Notion database URL or ID

        Returns:
            List of created document paths
        """
        # Extract database ID
        if "notion.so" in database_url_or_id:
            database_id = database_url_or_id.split("/")[-1].split("?")[0]
        else:
            database_id = database_url_or_id

        print(f"📚 Fetching database pages...")
        pages = self.notion.fetch_database_pages(database_id)
        print(f"   Found {len(pages)} pages")

        output_files = []
        for i, page in enumerate(pages, 1):
            try:
                print(f"\n[{i}/{len(pages)}] Processing page...")
                output_path = self.convert_page(page['id'])
                output_files.append(output_path)
            except Exception as e:
                logger.error(f"Failed to convert page {page['id']}: {e}")

        return output_files

    def _generate_output_path(self, title: str) -> str:
        """Generate a unique output path for the document"""
        safe_title = re.sub(r'[^\w\s-]', '', title)
        safe_title = re.sub(r'[-\s]+', '-', safe_title)[:50]  # Limit length

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{safe_title}_{timestamp}.docx"

        return os.path.join(self.output_dir, filename)