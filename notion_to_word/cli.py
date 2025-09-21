#!/usr/bin/env python3
"""
Notion to Word Converter
Main entry point for converting Notion pages to Word documents
"""

import os
import sys
import argparse
import logging
from dotenv import load_dotenv

from .converter import NotionToWordConverter

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'
)


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Convert Notion pages to Word documents',
        usage='%(prog)s [URL] [options]'
    )

    parser.add_argument(
        'url',
        nargs='?',
        help='Notion page URL or ID'
    )

    parser.add_argument(
        '--output', '-o',
        help='Output file path (default: auto-generated in outputs/)'
    )

    parser.add_argument(
        '--output-dir', '-d',
        default='outputs',
        help='Output directory (default: outputs/)'
    )

    parser.add_argument(
        '--template', '-t',
        default=None,
        help='Word template file path'
    )

    parser.add_argument(
        '--config', '-c',
        default='template_config.json',
        help='Template configuration JSON file'
    )

    parser.add_argument(
        '--no-template',
        action='store_true',
        help='Do not use a template'
    )

    parser.add_argument(
        '--database',
        action='store_true',
        help='Convert all pages in a database'
    )

    parser.add_argument(
        '--open',
        action='store_true',
        help='Open document after conversion (macOS only)'
    )

    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )

    args = parser.parse_args()

    # Set logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Get Notion token
    notion_token = os.getenv('NOTION_TOKEN')
    if not notion_token:
        print("❌ Error: NOTION_TOKEN not found in .env file")
        print("   Please set your Notion integration token")
        print("   Get it from: https://www.notion.so/my-integrations")
        sys.exit(1)

    # Handle template
    template_path = None if args.no_template else args.template

    # If no template specified, use default template
    if template_path is None and not args.no_template:
        default_template = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates", "default.docx")
        if os.path.exists(default_template):
            template_path = default_template

    if template_path and not os.path.exists(template_path):
        print(f"⚠️  Template not found: {template_path}")
        print("   Continuing without template...")
        template_path = None
    elif template_path:
        print(f"✨ Using template: {os.path.basename(template_path)}")

    # Get URL if not provided
    if not args.url:
        print("\n📋 Notion to Word Converter")
        print("-" * 40)
        args.url = input("Enter Notion page URL or ID: ").strip()
        if not args.url:
            print("❌ No URL provided")
            sys.exit(1)

    # Initialize converter
    try:
        converter = NotionToWordConverter(
            notion_token,
            template_path=template_path,
            output_dir=args.output_dir,
            config_path=args.config
        )
    except Exception as e:
        print(f"❌ Failed to initialize converter: {e}")
        sys.exit(1)

    # Perform conversion
    try:
        print(f"\n🚀 Starting conversion...")

        if args.database:
            print(f"   Converting database...")
            output_files = converter.convert_database(args.url)
            print(f"\n✨ Success! Converted {len(output_files)} documents")
            for path in output_files:
                print(f"   📁 {path}")
        else:
            output_path = converter.convert_page(args.url, args.output)
            print(f"\n✨ Success! Document created:")
            print(f"   📁 {output_path}")

            # Open if requested
            if args.open and sys.platform == "darwin":
                os.system(f'open "{output_path}"')
                print(f"   📂 Opening document...")

    except Exception as e:
        print(f"\n❌ Conversion failed: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        print("\nPlease check that:")
        print("  1. The page is shared with your integration")
        print("  2. The URL/ID is correct")
        print("  3. Your NOTION_TOKEN is valid")
        sys.exit(1)


if __name__ == "__main__":
    main()