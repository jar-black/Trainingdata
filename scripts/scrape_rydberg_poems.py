#!/usr/bin/env python3
"""
Web scraper for Viktor Rydberg poems from various sources.

Attempts to fetch poems from:
1. Project Runeberg (Swedish originals)
2. Archive.org mirrors
3. Alternative Swedish poetry sites

Usage:
    python scrape_rydberg_poems.py --fetch-all
    python scrape_rydberg_poems.py --poem tomten
"""

import argparse
import json
import time
import sys
from pathlib import Path
from typing import Optional, Dict, List

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Required packages not installed. Please run:")
    print("  pip install requests beautifulsoup4")
    sys.exit(1)


class RydbergPoemScraper:
    """Scraper for Viktor Rydberg poems."""

    DELAY = 2  # seconds between requests

    # Poem metadata from template
    POEMS = [
        {"swedish_title": "Tomten", "english_title": "The House-Goblin", "runeberg_slug": "tomten"},
        {"swedish_title": "Dexippos", "english_title": "Dexippus", "runeberg_slug": "dexippos"},
        {"swedish_title": "Skogsrået", "english_title": "The Wood Nymph", "runeberg_slug": "skogsr"},
        {"swedish_title": "Snöfrid", "english_title": "Snowfrid", "runeberg_slug": "snofrid"},
        {"swedish_title": "Korpen", "english_title": "The Raven", "runeberg_slug": "korpen"},
        {"swedish_title": "Drömliv", "english_title": "Dream Life", "runeberg_slug": "dromliv"},
        {"swedish_title": "På floden", "english_title": "On the River", "runeberg_slug": "pafloden"},
        {"swedish_title": "Kantat", "english_title": "Cantata", "runeberg_slug": "kantat"},
        {"swedish_title": "En blomma", "english_title": "A Flower", "runeberg_slug": "enblomma"},
        {"swedish_title": "Höstkväll", "english_title": "Autumn Evening", "runeberg_slug": "hostkvall"},
        {"swedish_title": "Den flygande holländaren", "english_title": "The Flying Dutchman", "runeberg_slug": "flygholl"},
        {"swedish_title": "Prometeus och Ahasverus", "english_title": "Prometheus and Ahasuerus", "runeberg_slug": "prometas"},
        {"swedish_title": "Till ödet", "english_title": "To Fate", "runeberg_slug": "tillodet"},
        {"swedish_title": "Vaknen!", "english_title": "Awaken!", "runeberg_slug": "vaknen"},
        {"swedish_title": "Drömmaren", "english_title": "The Dreamer", "runeberg_slug": "drommaren"},
        {"swedish_title": "Vadan och varthän?", "english_title": "Whence and Whither?", "runeberg_slug": "vadanvar"},
        {"swedish_title": "Älvan till flickan", "english_title": "The Elf to the Maiden", "runeberg_slug": "alvantil"},
        {"swedish_title": "Baldersbålet", "english_title": "Balder's Pyre", "runeberg_slug": "balders"},
        {"swedish_title": "Klockorna", "english_title": "The Bells", "runeberg_slug": "klockor"},
        {"swedish_title": "Vinst och förlust", "english_title": "Gain and Loss", "runeberg_slug": "vinstfor"},
        {"swedish_title": "De badande barnen", "english_title": "The Bathing Children", "runeberg_slug": None},
        {"swedish_title": "Den nya Grottesången", "english_title": "The New Grotti Song", "runeberg_slug": None},
    ]

    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Educational/Research Purpose)'
        })

    def scrape_from_runeberg(self, slug: str) -> Optional[str]:
        """Attempt to scrape Swedish text from Project Runeberg."""
        if not slug:
            return None

        url = f"https://runeberg.org/rydbdikt/{slug}.html"
        print(f"  Trying Runeberg: {url}")

        try:
            response = self.session.get(url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                # Try to find poem text (Runeberg typically uses specific tags)
                # Look for the main content area
                poem_text = None

                # Method 1: Look for <pre> tags
                pre_tag = soup.find('pre')
                if pre_tag:
                    poem_text = pre_tag.get_text()

                # Method 2: Look for paragraph content
                if not poem_text:
                    content_div = soup.find('div', class_='text')
                    if content_div:
                        poem_text = content_div.get_text()

                # Method 3: Get all paragraphs
                if not poem_text:
                    paragraphs = soup.find_all('p')
                    if paragraphs:
                        poem_text = '\n\n'.join([p.get_text() for p in paragraphs])

                if poem_text:
                    return poem_text.strip()
                else:
                    print(f"  Could not extract text from Runeberg page")
            elif response.status_code == 403:
                print(f"  Access denied (403) from Runeberg")
            else:
                print(f"  Failed with status {response.status_code}")
        except Exception as e:
            print(f"  Error: {e}")

        return None

    def scrape_from_heimskringla(self, title: str) -> Optional[str]:
        """Try to scrape from heimskringla.no (alternative source)."""
        # Create URL-friendly title
        url_title = title.replace(" ", "_").replace("å", "å").replace("ä", "ä").replace("ö", "ö")
        url = f"https://heimskringla.no/wiki/{url_title}_(Viktor_Rydberg)"
        print(f"  Trying Heimskringla: {url}")

        try:
            response = self.session.get(url, timeout=10)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                content = soup.find('div', {'id': 'mw-content-text'})
                if content:
                    # Extract poem text, skip navigation and metadata
                    poem_elem = content.find('pre') or content.find('poem')
                    if poem_elem:
                        return poem_elem.get_text().strip()
        except Exception as e:
            print(f"  Error: {e}")

        return None

    def scrape_poem(self, poem_meta: Dict) -> Dict:
        """Try to scrape a single poem from multiple sources."""
        print(f"\nScraping: {poem_meta['swedish_title']} / {poem_meta['english_title']}")

        swedish_text = None

        # Try Runeberg first
        if poem_meta.get('runeberg_slug'):
            swedish_text = self.scrape_from_runeberg(poem_meta['runeberg_slug'])
            time.sleep(self.DELAY)

        # Try heimskringla if Runeberg failed
        if not swedish_text:
            swedish_text = self.scrape_from_heimskringla(poem_meta['swedish_title'])
            time.sleep(self.DELAY)

        result = {
            "swedish_title": poem_meta['swedish_title'],
            "english_title": poem_meta['english_title'],
            "swedish_text": swedish_text if swedish_text else "[Could not fetch]",
            "english_text": "[To be fetched manually from Archive.org]",
            "collection": "Dikter",
            "year": None,
            "translator": "Charles Wharton Stork",
            "source_swedish": f"https://runeberg.org/rydbdikt/{poem_meta.get('runeberg_slug', '')}.html",
            "source_english": "Anthology of Swedish Lyrics (1917)",
            "fetch_success": swedish_text is not None
        }

        return result

    def scrape_all(self) -> List[Dict]:
        """Scrape all poems."""
        results = []
        success_count = 0

        for poem_meta in self.POEMS:
            result = self.scrape_poem(poem_meta)
            results.append(result)
            if result['fetch_success']:
                success_count += 1

        print(f"\n{'='*60}")
        print(f"Scraping complete!")
        print(f"Successfully fetched: {success_count}/{len(self.POEMS)} poems")
        print(f"Failed: {len(self.POEMS) - success_count} poems")
        print(f"{'='*60}\n")

        return results

    def save_results(self, results: List[Dict], output_dir: Path, jsonl_path: Path):
        """Save results to files."""
        output_dir.mkdir(parents=True, exist_ok=True)

        # Save individual poem files
        poem_num = 1
        for result in results:
            if result['swedish_text'] and result['swedish_text'] != "[Could not fetch]":
                swedish_file = output_dir / f"poem{poem_num}-swedish.txt"
                with open(swedish_file, 'w', encoding='utf-8') as f:
                    f.write(result['swedish_text'])
                print(f"Saved: {swedish_file}")

                # Create placeholder for English
                english_file = output_dir / f"poem{poem_num}-english.txt"
                with open(english_file, 'w', encoding='utf-8') as f:
                    f.write(f"[English translation for {result['english_title']} - to be added manually]\n")

                poem_num += 1

        # Save JSONL
        with open(jsonl_path, 'w', encoding='utf-8') as f:
            for result in results:
                # Remove fetch_success before saving
                result_clean = {k: v for k, v in result.items() if k != 'fetch_success'}
                f.write(json.dumps(result_clean, ensure_ascii=False) + '\n')

        print(f"\nSaved JSONL to: {jsonl_path}")


def main():
    parser = argparse.ArgumentParser(description='Scrape Viktor Rydberg poems')
    parser.add_argument('--fetch-all', action='store_true', help='Fetch all poems')
    parser.add_argument('--poem', help='Fetch specific poem by Swedish title')
    parser.add_argument('--output-dir', default='poems/rydberg', help='Output directory')
    parser.add_argument('--jsonl', default='data/rydberg_poems.jsonl', help='Output JSONL file')

    args = parser.parse_args()

    scraper = RydbergPoemScraper()

    if args.fetch_all:
        print("Fetching all 22 Viktor Rydberg poems...")
        print("Note: This may take a few minutes due to delays between requests.\n")
        results = scraper.scrape_all()
        scraper.save_results(results, Path(args.output_dir), Path(args.jsonl))
    elif args.poem:
        # Find poem in list
        poem_meta = next((p for p in scraper.POEMS if p['swedish_title'].lower() == args.poem.lower()), None)
        if poem_meta:
            result = scraper.scrape_poem(poem_meta)
            print(f"\nResult:")
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"Poem '{args.poem}' not found in list")
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
