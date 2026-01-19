#!/usr/bin/env python3
"""
Script to assist with collecting Erik Axel Karlfeldt poems from various sources.

This script provides helper functions to:
1. Parse poem texts from Archive.org downloads
2. Match Swedish originals with English translations
3. Create formatted poem files
4. Update the JSONL template

MANUAL STEPS REQUIRED:
1. Download "Anthology of Swedish Lyrics" (1917) from Archive.org
2. Download "Arcadia Borealis" (1938) from Archive.org
3. Access Projekt Runeberg for Swedish originals
4. Use this script to process and organize the texts

Author: Training Data Collection Project
Date: 2026-01-19
"""

import json
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional

# Base directories
BASE_DIR = Path("/home/user/Trainingdata")
DATA_DIR = BASE_DIR / "data"
POEMS_DIR = BASE_DIR / "poems" / "karlfeldt"
TEMPLATE_FILE = DATA_DIR / "karlfeldt_poems_template.jsonl"


def load_template() -> List[Dict]:
    """Load the poem metadata template."""
    poems = []
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                poems.append(json.loads(line))
    return poems


def save_template(poems: List[Dict]) -> None:
    """Save updated poem metadata template."""
    with open(TEMPLATE_FILE, 'w', encoding='utf-8') as f:
        for poem in poems:
            f.write(json.dumps(poem, ensure_ascii=False) + '\n')


def create_poem_file(filename: str, title: str, author: str,
                     collection: str, year: int, text: str,
                     translator: Optional[str] = None) -> None:
    """
    Create a formatted poem text file.

    Args:
        filename: Output filename (e.g., 'poem01-swedish.txt')
        title: Poem title
        author: Author name (Erik Axel Karlfeldt)
        collection: Collection name
        year: Publication year
        text: Full poem text
        translator: Translator name (for English versions)
    """
    filepath = POEMS_DIR / filename

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"Title: {title}\n")
        f.write(f"Author: {author}\n")
        f.write(f"Collection: {collection}\n")
        f.write(f"Year: {year}\n")
        if translator:
            f.write(f"Translator: {translator}\n")
        f.write("\n")
        f.write(text.strip())
        f.write("\n")

    print(f"Created: {filepath}")


def parse_archive_org_text(text: str, poem_title: str) -> Optional[str]:
    """
    Parse a poem from Archive.org plain text export.

    This is a helper function to extract individual poems from
    downloaded Archive.org full text files.

    Args:
        text: Full text content from Archive.org
        poem_title: Title of the poem to extract

    Returns:
        Extracted poem text or None if not found
    """
    # This is a placeholder - actual implementation will depend on
    # the format of the Archive.org text export
    lines = text.split('\n')

    # Look for title
    start_idx = None
    for i, line in enumerate(lines):
        if poem_title.upper() in line.upper():
            start_idx = i
            break

    if start_idx is None:
        return None

    # Extract poem (until next title or separator)
    poem_lines = []
    for line in lines[start_idx + 1:]:
        if line.strip() and (line.isupper() or line.startswith('---')):
            break
        poem_lines.append(line)

    return '\n'.join(poem_lines).strip()


def match_swedish_english(swedish_title: str, english_title: str) -> bool:
    """
    Verify that Swedish and English titles match.

    Returns True if they appear to be translations of each other.
    """
    # Simple length-based check
    if abs(len(swedish_title) - len(english_title)) > 20:
        return False

    # Could add more sophisticated matching here
    return True


def create_poem_pair(poem_data: Dict, poem_number: int,
                     swedish_text: str, english_text: str) -> None:
    """
    Create a matched pair of Swedish and English poem files.

    Args:
        poem_data: Metadata dictionary from template
        poem_number: Sequential poem number (1, 2, 3, ...)
        swedish_text: Full Swedish poem text
        english_text: Full English poem text
    """
    # Create Swedish file
    swedish_filename = f"poem{poem_number:02d}-swedish.txt"
    create_poem_file(
        filename=swedish_filename,
        title=poem_data['swedish_title'],
        author="Erik Axel Karlfeldt",
        collection=poem_data['collection'],
        year=poem_data['year'],
        text=swedish_text
    )

    # Create English file
    english_filename = f"poem{poem_number:02d}-english.txt"
    create_poem_file(
        filename=english_filename,
        title=poem_data['english_title'],
        author="Erik Axel Karlfeldt",
        collection=poem_data['collection'],
        year=poem_data['year'],
        text=english_text,
        translator=poem_data['translator']
    )

    # Update template with actual texts
    poem_data['swedish_text'] = swedish_text
    poem_data['english_text'] = english_text


def extract_from_runeberg_html(html_content: str) -> str:
    """
    Extract poem text from Projekt Runeberg HTML.

    Args:
        html_content: Raw HTML content from Runeberg.org

    Returns:
        Cleaned poem text
    """
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', html_content)

    # Remove excess whitespace
    text = re.sub(r'\n\s*\n', '\n\n', text)

    return text.strip()


def validate_poem_file(filepath: Path) -> bool:
    """
    Validate that a poem file is properly formatted.

    Checks:
    - File exists and is readable
    - Contains required metadata headers
    - Has non-empty poem text

    Returns:
        True if valid, False otherwise
    """
    if not filepath.exists():
        print(f"Error: {filepath} does not exist")
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check for required headers
    required = ['Title:', 'Author:', 'Collection:', 'Year:']
    for req in required:
        if req not in content:
            print(f"Error: {filepath} missing '{req}' header")
            return False

    # Check for poem text (after headers)
    lines = content.split('\n')
    text_started = False
    has_text = False

    for line in lines:
        if text_started and line.strip():
            has_text = True
            break
        if line.strip() == '':
            text_started = True

    if not has_text:
        print(f"Error: {filepath} has no poem text")
        return False

    return True


def generate_collection_report() -> Dict:
    """
    Generate a report on collection progress.

    Returns:
        Dictionary with statistics about collected poems
    """
    template = load_template()

    report = {
        'total_poems_in_template': len(template),
        'poems_with_swedish_text': 0,
        'poems_with_english_text': 0,
        'complete_pairs': 0,
        'swedish_files': 0,
        'english_files': 0,
        'collections_represented': set()
    }

    # Check template
    for poem in template:
        if poem['swedish_text'] != '[To be filled]' and poem['swedish_text'] != '[To be filled with Swedish original]':
            report['poems_with_swedish_text'] += 1
        if poem['english_text'] != '[To be filled]' and poem['english_text'] != '[To be filled with English translation]':
            report['poems_with_english_text'] += 1
        if report['poems_with_swedish_text'] == report['poems_with_english_text']:
            report['complete_pairs'] += 1
        report['collections_represented'].add(poem['collection'])

    # Check files
    if POEMS_DIR.exists():
        swedish_files = list(POEMS_DIR.glob('*-swedish.txt'))
        english_files = list(POEMS_DIR.glob('*-english.txt'))
        report['swedish_files'] = len(swedish_files)
        report['english_files'] = len(english_files)

    report['collections_represented'] = list(report['collections_represented'])

    return report


def print_report() -> None:
    """Print a formatted collection progress report."""
    report = generate_collection_report()

    print("\n" + "=" * 60)
    print("KARLFELDT POEM COLLECTION PROGRESS REPORT")
    print("=" * 60)
    print(f"\nTemplate Status:")
    print(f"  Total poems in template: {report['total_poems_in_template']}")
    print(f"  Poems with Swedish text: {report['poems_with_swedish_text']}")
    print(f"  Poems with English text: {report['poems_with_english_text']}")
    print(f"  Complete pairs: {report['complete_pairs']}")

    print(f"\nFile Status:")
    print(f"  Swedish text files: {report['swedish_files']}")
    print(f"  English text files: {report['english_files']}")

    print(f"\nCollections Represented:")
    for collection in sorted(report['collections_represented']):
        print(f"  - {collection}")

    print("\n" + "=" * 60)

    # Calculate percentage
    if report['total_poems_in_template'] > 0:
        percentage = (report['complete_pairs'] / report['total_poems_in_template']) * 100
        print(f"\nProgress: {percentage:.1f}% complete")
        print(f"Target: 25-30 poem pairs")
        print(f"Current: {report['complete_pairs']} pairs")

    print("=" * 60 + "\n")


def main():
    """Main function - prints usage instructions."""
    print("\nKarlfeldt Poem Collection Helper Script")
    print("=" * 60)
    print("\nThis script provides helper functions for collecting and")
    print("organizing Erik Axel Karlfeldt poems.")
    print("\nAvailable functions:")
    print("  - load_template(): Load poem metadata")
    print("  - create_poem_file(): Create formatted poem text file")
    print("  - create_poem_pair(): Create Swedish/English pair")
    print("  - parse_archive_org_text(): Extract from Archive.org text")
    print("  - extract_from_runeberg_html(): Extract from Runeberg HTML")
    print("  - validate_poem_file(): Check file formatting")
    print("  - print_report(): Show collection progress")
    print("\nTo use: import this file as a module or edit it to add")
    print("        specific collection code.")
    print("\nCurrent status:")
    print_report()


if __name__ == "__main__":
    main()
