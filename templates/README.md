# Word Templates

This directory contains Word document templates for styling your converted Notion pages.

## Adding Your Own Template

1. Create a Word document with your desired styles (Heading 1, Heading 2, Normal, etc.)
2. Configure fonts, colors, and formatting
3. Save as `your-template.docx` in this directory
4. Update `config/styles.json` to map Notion blocks to your Word styles
5. Use with: `uv run notion-to-word "URL" --template "templates/your-template.docx"`

## Template Requirements

Your template should include these styles:
- **Title** - For page titles
- **Heading 1, 2, 3** - For section headers
- **Normal** - For regular text
- **List Paragraph** - For bulleted lists
- **Quote** - For quote blocks
- **Code** - For code blocks

## Example Style Mapping

Edit `config/styles.json`:

```json
{
  "templates": {
    "your_template": {
      "name": "Your Template",
      "path": "templates/your-template.docx",
      "style_mappings": {
        "title": "Title",
        "heading_1": "Heading 1",
        "paragraph": "Normal",
        "quote": "Quote"
      }
    }
  }
}
```

**Note**: Company-specific templates are gitignored for privacy.