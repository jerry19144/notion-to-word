"""
Configuration management for Notion to Word converter
"""

import os
import json
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)


class TemplateConfig:
    """Manages template configuration and style mappings"""

    def __init__(self, config_path: str = None):
        """Load template configuration from JSON file"""
        if config_path is None:
            # Use relative path from package root
            config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", "styles.json")
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self) -> Dict:
        """Load configuration from JSON file"""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError as e:
                logger.error(f"Error parsing config file: {e}")
                return self._default_config()
        else:
            logger.warning(f"Config file not found: {self.config_path}, using defaults")
            return self._default_config()

    def _default_config(self) -> Dict:
        """Return default configuration if file not found"""
        return {
            "templates": {
                "default": {
                    "name": "Default Template",
                    "path": None,
                    "font": "Calibri",
                    "style_mappings": {
                        "title": "Title",
                        "heading_1": "Heading 1",
                        "heading_2": "Heading 2",
                        "heading_3": "Heading 3",
                        "heading_4": "Heading 4",
                        "heading_5": "Heading 5",
                        "paragraph": "Normal",
                        "bulleted_list_item": "Normal",
                        "numbered_list_item": "Normal",
                        "to_do": "Normal",
                        "code": "Normal",
                        "quote": "Normal",
                        "callout": "Normal",
                        "default": "Normal"
                    },
                    "formatting": {
                        "title_alignment": "center",
                        "title_size": 18,
                        "code_font": "Courier New",
                        "code_size": 10,
                        "metadata_size": 10,
                        "metadata_color": "#666666",
                        "bullet_symbol": "•",
                        "checkbox_checked": "☑",
                        "checkbox_unchecked": "☐",
                        "toggle_symbol": "▶",
                        "quote_left": "\u201c",
                        "quote_right": "\u201d"
                    }
                }
            }
        }

    def get_template(self, template_name: str = "default") -> Dict:
        """Get template configuration by name"""
        templates = self.config.get("templates", {})
        return templates.get(template_name, templates.get("default", {}))

    def get_style_for_block(self, block_type: str, template_name: str = "default") -> str:
        """Get Word style for a Notion block type with fallback"""
        template = self.get_template(template_name)
        mappings = template.get("style_mappings", {})

        # Try exact match first
        if block_type in mappings:
            return mappings[block_type]

        # Fall back to default
        return mappings.get("default", "Normal")