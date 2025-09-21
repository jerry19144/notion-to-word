#!/usr/bin/env python3
"""
Non-interactive test runner for the Notion to Word converter
"""

import os
import sys
import json
from datetime import datetime
from docx import Document

from notion_to_word.notion_client import NotionClient
from notion_to_word.config import TemplateConfig
from notion_to_word.word_formatter import WordFormatter
from notion_to_word.converter import NotionToWordConverter


def run_tests():
    """Run all non-interactive tests"""
    print("\n" + "="*60)
    print(" NOTION TO WORD CONVERTER - AUTOMATED TESTS")
    print("="*60)

    results = {
        "passed": 0,
        "failed": 0,
        "total": 0
    }

    # Test 1: Environment
    print("\n[TEST] Environment Setup")
    results["total"] += 3

    if os.path.exists(".env"):
        print("  ✓ .env file exists")
        results["passed"] += 1
    else:
        print("  ✗ .env file missing")
        results["failed"] += 1

    from dotenv import load_dotenv
    load_dotenv()
    token = os.getenv('NOTION_TOKEN')

    if token:
        print("  ✓ NOTION_TOKEN found")
        results["passed"] += 1
    else:
        print("  ✗ NOTION_TOKEN missing")
        results["failed"] += 1

    template_path = os.path.join("..", "templates", "default.docx")
    if os.path.exists(template_path) or os.path.exists("templates/default.docx"):
        print("  ✓ Template file found")
        results["passed"] += 1
    else:
        print("  ✗ Template file missing")
        results["failed"] += 1

    # Test 2: URL Parsing
    print("\n[TEST] URL Parsing")
    test_cases = [
        ("274e531aede680e9a2a7c31931ae355e", "274e531aede680e9a2a7c31931ae355e"),
        ("https://notion.so/Page-274e531aede680e9a2a7c31931ae355e", "274e531aede680e9a2a7c31931ae355e"),
    ]

    for url, expected in test_cases:
        results["total"] += 1
        page_id, _ = NotionClient.extract_page_id(url)
        if page_id == expected:
            print(f"  ✓ Parse: {url[:40]}...")
            results["passed"] += 1
        else:
            print(f"  ✗ Parse failed: {url[:40]}...")
            results["failed"] += 1

    # Test 3: Configuration
    print("\n[TEST] Configuration Loading")
    results["total"] += 2

    try:
        config = TemplateConfig()  # Use default config path
        print("  ✓ Config file loaded")
        results["passed"] += 1

        style = config.get_style_for_block("paragraph", "ic_template")
        if style == "Normal":
            print(f"  ✓ Style mapping works: paragraph → {style}")
            results["passed"] += 1
        else:
            print("  ✗ Style mapping failed")
            results["failed"] += 1
    except Exception as e:
        print(f"  ✗ Config error: {e}")
        results["failed"] += 2

    # Test 4: Document Creation
    print("\n[TEST] Document Creation")
    results["total"] += 2

    try:
        formatter = WordFormatter({"font": "Aptos", "formatting": {}})
        doc = formatter.create_document()
        print("  ✓ Create blank document")
        results["passed"] += 1

        test_file = "outputs/test.docx"
        formatter.add_title(doc, "Test")
        doc.save(test_file)

        if os.path.exists(test_file):
            print("  ✓ Save document")
            results["passed"] += 1
            os.remove(test_file)
        else:
            print("  ✗ Save failed")
            results["failed"] += 1
    except Exception as e:
        print(f"  ✗ Document creation error: {e}")
        results["failed"] += 2

    # Test 5: Notion Connection (if token available)
    if token:
        print("\n[TEST] Notion API Connection")
        results["total"] += 1

        try:
            from notion_client import Client
            client = Client(auth=token)
            response = client.search(filter={"property": "object", "value": "page"})

            if response:
                count = len(response.get('results', []))
                print(f"  ✓ API connected ({count} pages found)")
                results["passed"] += 1
            else:
                print("  ✗ API connection failed")
                results["failed"] += 1
        except Exception as e:
            print(f"  ✗ API error: {str(e)[:50]}...")
            results["failed"] += 1
    else:
        print("\n[SKIP] Notion API Connection (no token)")

    # Print summary
    print("\n" + "="*60)
    print(" TEST SUMMARY")
    print("="*60)
    print(f"\n  Total:  {results['total']} tests")
    print(f"  Passed: {results['passed']} ✓")
    print(f"  Failed: {results['failed']} ✗")

    if results['failed'] == 0:
        print("\n  🎉 All tests passed!")
        return 0
    else:
        print(f"\n  ⚠️  {results['failed']} test(s) failed")
        return 1


if __name__ == "__main__":
    exit_code = run_tests()
    sys.exit(exit_code)