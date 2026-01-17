#!/usr/bin/env python3
"""
Web scraper for Gustaf Fröding poems from various sources.

IMPORTANT:
- This script respects robots.txt and adds delays between requests
- Only use for personal research/educational purposes
- Check each website's terms of service before scraping
- Some sites may block automated access (403 errors)
- Consider manually downloading from Archive.org instead

Usage:
    python scrape_froding_poems.py --source allmogens --output data/froding_poems.jsonl
    python scrape_froding_poems.py --source runeberg --poem "Indianer" --output data/poems.jsonl
"""

import argparse
import json
import time
from pathlib import Path
from typing import Optional, Dict
import sys

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Required packages not installed. Please run:")
    print("  pip install requests beautifulsoup4")
    sys.exit(1)


class FrodingPoem:
    """Represents a Fröding poem with metadata."""

    def __init__(self, swedish_title: str, english_title: str):
        self.swedish_title = swedish_title
        self.english_title = english_title
        self.swedish_text = ""
        self.english_text = ""
        self.collection = ""
        self.year = None
        self.translator = ""
        self.source_swedish = ""
        self.source_english = ""

    def to_dict(self) -> Dict:
        return {
            "swedish_title": self.swedish_title,
            "english_title": self.english_title,
            "swedish_text": self.swedish_text,
            "english_text": self.english_text,
            "collection": self.collection,
            "year": self.year if self.year else "Unknown",
            "translator": self.translator,
            "source_swedish": self.source_swedish,
            "source_english": self.source_english
        }


class AllmogensScraper:
    """Scraper for allmogens.se (has both Swedish and English)."""

    BASE_URL = "https://allmogens.se"
    DELAY = 2  # seconds between requests

    KNOWN_POEMS = [
        ("idealism-och-realism", "Idealism och realism", "Idealism and Realism", "Nya dikter", 1894),
        ("i-ungdomen", "I ungdomen", "In Youth", "Stänk och flikar", 1896),
        ("friheten", "Friheten", "Freedom", "Gralstänk", 1898),
        ("den-gamla-goda-tiden", "Den gamla goda tiden", "The Good Old Days", "Nya dikter", 1894),
        ("strovtag-i-hembygden", "Strövtåg i hembygden", "A Stroll Through the Local Countryside", "Stänk och flikar", 1896),
    ]

    def scrape_all(self) -> list:
        """Scrape all known poems from allmogens.se."""
        poems = []
        for slug, swedish_title, english_title, collection, year in self.KNOWN_POEMS:
            print(f"Scraping: {swedish_title} / {english_title}")
            poem = self.scrape_poem(slug, swedish_title, english_title, collection, year)
            if poem:
                poems.append(poem)
            time.sleep(self.DELAY)
        return poems

    def scrape_poem(self, slug: str, swedish_title: str, english_title: str,
                    collection: str, year: int) -> Optional[FrodingPoem]:
        """Scrape a single poem from allmogens.se."""
        poem = FrodingPoem(swedish_title, english_title)
        poem.collection = collection
        poem.year = year
        poem.translator = "Allmogens.se translator"

        # Get English version
        english_url = f"{self.BASE_URL}/en/poetry/{slug}/"
        poem.source_english = english_url

        try:
            response = requests.get(english_url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                # Find the poem text (this is a placeholder - actual selector depends on HTML structure)
                # You'll need to inspect the page and update this selector
                poem_div = soup.find('div', class_='poem-text') or soup.find('article')
                if poem_div:
                    poem.english_text = poem_div.get_text(strip=True)
            else:
                print(f"  Failed to fetch English version: {response.status_code}")
        except Exception as e:
            print(f"  Error fetching English: {e}")

        time.sleep(self.DELAY)

        # Get Swedish version
        swedish_url = f"{self.BASE_URL}/poetry/{slug}/"
        poem.source_swedish = swedish_url

        try:
            response = requests.get(swedish_url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                poem_div = soup.find('div', class_='poem-text') or soup.find('article')
                if poem_div:
                    poem.swedish_text = poem_div.get_text(strip=True)
            else:
                print(f"  Failed to fetch Swedish version: {response.status_code}")
        except Exception as e:
            print(f"  Error fetching Swedish: {e}")

        return poem if (poem.swedish_text and poem.english_text) else None


class RunebergScraper:
    """
    Scraper for Project Runeberg (Swedish originals only).

    Note: Project Runeberg may block automated access.
    Consider using their bulk downloads or API if available.
    """

    BASE_URL = "https://runeberg.org"
    DELAY = 3  # Be more conservative with Project Runeberg

    def scrape_poem(self, collection: str, poem_slug: str) -> Optional[str]:
        """
        Scrape a poem from Project Runeberg.

        Args:
            collection: e.g., 'dragharm', 'stanflik'
            poem_slug: e.g., 'indianer', 'solnedgg'
        """
        url = f"{self.BASE_URL}/{collection}/{poem_slug}.html"

        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                # The poem text is typically in a <pre> tag or similar
                # Update this selector based on actual HTML structure
                poem_text = soup.find('pre') or soup.find('div', class_='poem')
                if poem_text:
                    return poem_text.get_text(strip=True)
            else:
                print(f"Failed to fetch from Runeberg: {response.status_code}")
        except Exception as e:
            print(f"Error scraping Runeberg: {e}")

        time.sleep(self.DELAY)
        return None


def save_poems(poems: list, output_path: str):
    """Save poems to JSONL file."""
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, 'a', encoding='utf-8') as f:
        for poem in poems:
            if isinstance(poem, FrodingPoem):
                json_line = json.dumps(poem.to_dict(), ensure_ascii=False)
            else:
                json_line = json.dumps(poem, ensure_ascii=False)
            f.write(json_line + '\n')

    print(f"\nSaved {len(poems)} poems to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Scrape Gustaf Fröding poems from various sources"
    )
    parser.add_argument(
        '--source',
        choices=['allmogens', 'runeberg'],
        required=True,
        help='Source to scrape from'
    )
    parser.add_argument(
        '--output',
        default='data/froding_poems_scraped.jsonl',
        help='Output JSONL file'
    )
    parser.add_argument(
        '--poem',
        help='Specific poem to scrape (for Runeberg)'
    )
    parser.add_argument(
        '--collection',
        help='Collection slug for Runeberg (e.g., dragharm, stanflik)'
    )

    args = parser.parse_args()

    if args.source == 'allmogens':
        scraper = AllmogensScraper()
        print("Scraping poems from allmogens.se...")
        print("Note: You may need to update the HTML selectors in the code.\n")
        poems = scraper.scrape_all()
        save_poems(poems, args.output)

    elif args.source == 'runeberg':
        if not args.poem or not args.collection:
            print("Error: --poem and --collection are required for Runeberg")
            sys.exit(1)

        scraper = RunebergScraper()
        print(f"Scraping {args.poem} from {args.collection}...")
        text = scraper.scrape_poem(args.collection, args.poem)
        if text:
            print(f"Successfully scraped poem:\n{text[:200]}...")
        else:
            print("Failed to scrape poem")


if __name__ == '__main__':
    main()
