#!/usr/bin/env python3
"""
Collect Esaias Tegnér (1782-1846) poems with Swedish originals and English translations.

Sources (all public domain):
1. Swedish Wikisource - https://sv.wikisource.org/wiki/Författare:Esaias_Tegnér
2. English Wikisource - https://en.wikisource.org/wiki/Author:Esaias_Tegnér
3. Projekt Runeberg - http://runeberg.org/authors/tegner.html
4. Anthology of Swedish Lyrics (1917) - Charles Wharton Stork
5. svenskadikter.com - Swedish poetry database
"""

import requests
from bs4 import BeautifulSoup
import json
import time
import os
import re
from pathlib import Path

class TegnerCollector:
    def __init__(self, output_dir="/home/user/Trainingdata/poems/tegner"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

        # Known poems from research
        self.known_poems = {
            'svea': {
                'swedish_title': 'Svea',
                'english_title': 'Svea',
                'swedish_url': 'https://sv.wikisource.org/wiki/Svea',
                'year': 1811,
                'notes': 'Patriotic poem that won Swedish Academy prize'
            },
            'nattvardsbarn': {
                'swedish_title': 'Nattvardsbarn',
                'english_title': "The Children of the Lord's Supper",
                'swedish_url': 'http://runeberg.org/tepoems/',
                'english_url': 'https://allpoetry.com/The-Children-Of-The-Lord\'s-Supper',
                'year': 1820,
                'translator': 'Henry Wadsworth Longfellow',
                'notes': 'Major work translated by Longfellow in 1841'
            },
            'frithiof': {
                'swedish_title': 'Frithiofs saga',
                'english_title': "Frithiof's Saga",
                'english_url': 'http://runeberg.org/tepoems/',
                'year': 1825,
                'translator': 'Rev. W. Lewery Blackley',
                'notes': 'Epic poem, his masterpiece'
            },
            'flyttfaglarna': {
                'swedish_title': 'Flyttfåglarna',
                'english_title': 'Birds of Passage',
                'swedish_url': 'https://svenskadikter.com/Flyttfåglarna_(Tegnér)',
                'notes': 'Mock-celebration of poets who migrate south'
            },
            'jatten': {
                'swedish_title': 'Jätten',
                'english_title': 'The Giant',
                'notes': 'Mentioned in Stork anthology'
            },
            'det_eviga': {
                'swedish_title': 'Det eviga',
                'english_title': 'The Eternal',
                'notes': 'In Stork anthology'
            },
            'sang_till_solen': {
                'swedish_title': 'Sång till solen',
                'english_title': 'Song to the Sun',
                'swedish_url': 'https://sv.wikisource.org/wiki/Sång_till_solen',
                'year': 1817,
                'notes': 'Celebrated hymn to the sun'
            },
            'epilog_1820': {
                'swedish_title': 'Epilog vid magisterpromotionen i Lund 1820',
                'english_title': 'Epilogue at the Master Promotion in Lund 1820',
                'swedish_url': 'https://sv.wikisource.org/wiki/Epilog_vid_magisterpromotionen_i_Lund_1820',
                'year': 1820
            },
            'den_dode': {
                'swedish_title': 'Den döde',
                'english_title': 'The Dead',
                'swedish_url': 'https://sv.wikisource.org/wiki/Den_döde'
            },
            'axel': {
                'swedish_title': 'Axel',
                'english_title': 'Axel',
                'translator': 'Oscar Baker',
                'notes': 'Narrative poem about Charles XII'
            }
        }

    def fetch_page(self, url, delay=2):
        """Fetch a webpage with rate limiting"""
        time.sleep(delay)
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response.text
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None

    def extract_wikisource_poem(self, html):
        """Extract poem text from Wikisource page"""
        soup = BeautifulSoup(html, 'html.parser')

        # Try to find the poem content
        poem_div = soup.find('div', class_='poem')
        if poem_div:
            return poem_div.get_text(strip=False)

        # Alternative: look for mw-parser-output
        content = soup.find('div', class_='mw-parser-output')
        if content:
            # Remove navigation, metadata, etc.
            for tag in content.find_all(['table', 'div'], class_=['infobox', 'navbox', 'metadata']):
                tag.decompose()
            return content.get_text(strip=False)

        return None

    def collect_from_wikisource_swedish(self):
        """Collect Swedish originals from Swedish Wikisource"""
        print("Collecting from Swedish Wikisource...")

        for poem_id, data in self.known_poems.items():
            if 'swedish_url' in data and 'wikisource' in data['swedish_url']:
                print(f"  Fetching {data['swedish_title']}...")
                html = self.fetch_page(data['swedish_url'])
                if html:
                    poem_text = self.extract_wikisource_poem(html)
                    if poem_text:
                        filename = f"{poem_id}-swedish.txt"
                        filepath = self.output_dir / filename
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(poem_text)
                        print(f"    ✓ Saved to {filename}")
                    else:
                        print(f"    ✗ Could not extract poem text")

    def collect_from_svenskadikter(self):
        """Collect from svenskadikter.com"""
        print("Collecting from svenskadikter.com...")

        for poem_id, data in self.known_poems.items():
            if 'swedish_url' in data and 'svenskadikter' in data['swedish_url']:
                print(f"  Fetching {data['swedish_title']}...")
                html = self.fetch_page(data['swedish_url'])
                if html:
                    soup = BeautifulSoup(html, 'html.parser')
                    # svenskadikter.com specific extraction
                    poem_div = soup.find('div', class_='mw-parser-output')
                    if poem_div:
                        poem_text = poem_div.get_text(strip=False)
                        filename = f"{poem_id}-swedish.txt"
                        filepath = self.output_dir / filename
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(poem_text)
                        print(f"    ✓ Saved to {filename}")

    def collect_from_runeberg(self):
        """Collect from Projekt Runeberg"""
        print("Collecting from Projekt Runeberg...")

        # Runeberg has "Poems by Tegnér" book with both works
        base_url = "http://runeberg.org/tepoems/"

        # This would need page-by-page collection
        # The book structure needs to be navigated
        print("  Note: Runeberg requires page-by-page collection")
        print("  Manual collection recommended for this source")

    def save_metadata(self):
        """Save poem metadata to JSONL file"""
        metadata_file = "/home/user/Trainingdata/data/tegner_poems_template.jsonl"

        with open(metadata_file, 'w', encoding='utf-8') as f:
            for poem_id, data in self.known_poems.items():
                entry = {
                    'poem_id': poem_id,
                    'swedish_title': data.get('swedish_title', ''),
                    'english_title': data.get('english_title', ''),
                    'year': data.get('year', None),
                    'translator': data.get('translator', ''),
                    'swedish_file': f"{poem_id}-swedish.txt" if 'swedish_url' in data else '',
                    'english_file': f"{poem_id}-english.txt" if 'english_url' in data else '',
                    'source_swedish': data.get('swedish_url', ''),
                    'source_english': data.get('english_url', ''),
                    'notes': data.get('notes', ''),
                    'author': 'Esaias Tegnér',
                    'author_years': '1782-1846',
                    'language_pair': 'sv-en'
                }
                f.write(json.dumps(entry, ensure_ascii=False) + '\n')

        print(f"\n✓ Metadata saved to {metadata_file}")

    def create_readme(self):
        """Create README with source information"""
        readme_path = self.output_dir / "README.md"

        readme_content = """# Esaias Tegnér (1782-1846) - Poem Collection

## About Esaias Tegnér

Esaias Tegnér was a Swedish writer, professor of Greek language, and bishop. During the 19th century, he was regarded as the father of modern poetry in Sweden. His most famous work is the epic poem "Frithiof's Saga" (1825), which has been translated into English numerous times.

## Sources (All Public Domain)

### Swedish Originals:

1. **Swedish Wikisource** - https://sv.wikisource.org/wiki/Författare:Esaias_Tegnér
   - Complete texts of major poems including "Svea", "Sång till solen"

2. **Projekt Runeberg** - http://runeberg.org/authors/tegner.html
   - Digital library of Scandinavian literature
   - "Samlade skrifter" (Collected Works)
   - Individual poem collections

3. **svenskadikter.com** - Swedish poetry database
   - Various shorter poems

### English Translations:

1. **English Wikisource** - https://en.wikisource.org/wiki/Author:Esaias_Tegnér
   - "The Children of the Lord's Supper" (trans. Longfellow)
   - "Frithiof's Saga" (various translators)

2. **"Poems by Tegnér" (1914)** - American-Scandinavian Foundation
   - Internet Archive: https://archive.org/details/poemsbytegnrch00tegnuoft
   - "The Children of the Lord's Supper" - trans. Henry Wadsworth Longfellow
   - "Frithiof's Saga" - trans. Rev. W. Lewery Blackley
   - Also on Projekt Runeberg: http://runeberg.org/tepoems/

3. **"Anthology of Swedish Lyrics from 1750 to 1915" (1917)**
   - Compiled and translated by Charles Wharton Stork
   - Internet Archive: https://archive.org/details/anthologyofswedi00stor
   - Contains 13+ Tegnér poems including:
     - "Birds of Passage" (Flyttfåglarna)
     - "The Giant" (Jätten)
     - "The Eternal" (Det eviga)
     - "Song to the Sun" (Sång till solen)
     - Other shorter lyrics

4. **"Specimens of Swedish and German Poetry" (1848)**
   - Translator: John Elliot Drinkwater Bethune
   - Internet Archive: https://archive.org/details/specimensswedis00bethgoog

5. **"Axel, and Svea" (1882)**
   - Translator: Oscar Baker
   - Google Books available

## Major Works

### 1. Frithiofs saga (Frithiof's Saga) - 1825
- Tegnér's masterpiece
- Epic romance cycle based on Old Norse legend
- Translated into English 20+ times
- 24 cantos telling the story of Frithiof and Ingeborg

### 2. Nattvardsbarn (The Children of the Lord's Supper) - 1820
- Long narrative poem about confirmation
- Famous English translation by Henry Wadsworth Longfellow (1841)
- Made Tegnér internationally known

### 3. Svea - 1811
- Patriotic poem about Sweden's loss of Finland
- Won the Swedish Academy's grand prize
- Made Tegnér famous in Sweden

### 4. Sång till solen (Song to the Sun) - 1817
- Celebrated hymn to the sun
- Inspired Carl Milles' sculpture "The Sun Singer"

## Shorter Lyrics

- Flyttfåglarna (Birds of Passage)
- Jätten (The Giant)
- Det eviga (The Eternal)
- Den döde (The Dead)
- Axel - Narrative poem about Charles XII
- Epilog vid magisterpromotionen i Lund 1820

## Collection Status

Total poems identified: 10+
Poems with Swedish original: Available on Wikisource and Runeberg
Poems with English translation: Available in various anthologies
Complete pairs (Swedish + English): Work in progress

## File Format

- Swedish originals: `{poem_id}-swedish.txt`
- English translations: `{poem_id}-english.txt`
- Metadata: `../data/tegner_poems_template.jsonl`

## Notes

All sources are in the public domain. Tegnér died in 1846, and most translations are from the 19th and early 20th centuries.

## Collection Script

See `../scripts/collect_tegner_poems.py` for the automated collection script.
"""

        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)

        print(f"✓ README created at {readme_path}")

    def run(self):
        """Run the full collection process"""
        print("=" * 70)
        print("Esaias Tegnér Poem Collection Script")
        print("=" * 70)
        print()

        # Create metadata first
        self.save_metadata()

        # Create README
        self.create_readme()

        # Collect poems
        self.collect_from_wikisource_swedish()
        self.collect_from_svenskadikter()
        self.collect_from_runeberg()

        print("\n" + "=" * 70)
        print("Collection complete!")
        print(f"Output directory: {self.output_dir}")
        print("=" * 70)

if __name__ == "__main__":
    collector = TegnerCollector()
    collector.run()
