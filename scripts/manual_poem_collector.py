#!/usr/bin/env python3
"""
Manual poem collection helper for Gustaf Fröding poems.

This script helps you manually collect poems by:
1. Prompting you to paste Swedish and English versions
2. Creating individual poemN-swedish.txt and poemN-english.txt files
3. Tracking progress and allowing you to resume
4. Updating the JSONL database

Usage:
    python3 scripts/manual_poem_collector.py
    python3 scripts/manual_poem_collector.py --output-dir poems/froding
    python3 scripts/manual_poem_collector.py --resume
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime

class PoemCollector:
    def __init__(self, output_dir="poems/froding", jsonl_path="data/froding_poems.jsonl", template_path="data/froding_poems_template.jsonl"):
        self.output_dir = Path(output_dir)
        self.jsonl_path = Path(jsonl_path)
        self.template_path = Path(template_path)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def load_template(self):
        """Load the template with poem metadata."""
        poems = []
        if self.template_path.exists():
            with open(self.template_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        poems.append(json.loads(line))
        return poems

    def load_existing_poems(self):
        """Load existing collected poems."""
        poems = []
        if self.jsonl_path.exists():
            with open(self.jsonl_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        poems.append(json.loads(line))
        return poems

    def get_next_poem_number(self):
        """Find the next available poem number."""
        existing_files = list(self.output_dir.glob("poem*-swedish.txt"))
        if not existing_files:
            return 1

        numbers = []
        for f in existing_files:
            try:
                num = int(f.stem.split('-')[0].replace('poem', ''))
                numbers.append(num)
            except:
                continue

        return max(numbers) + 1 if numbers else 1

    def save_poem_files(self, poem_num, swedish_text, english_text):
        """Save poem to individual text files."""
        swedish_file = self.output_dir / f"poem{poem_num}-swedish.txt"
        english_file = self.output_dir / f"poem{poem_num}-english.txt"

        with open(swedish_file, 'w', encoding='utf-8') as f:
            f.write(swedish_text)

        with open(english_file, 'w', encoding='utf-8') as f:
            f.write(english_text)

        return swedish_file, english_file

    def update_jsonl(self, poem_data):
        """Update or append to JSONL file."""
        existing_poems = self.load_existing_poems()

        # Check if poem already exists (by title)
        found = False
        for i, existing in enumerate(existing_poems):
            if existing.get('swedish_title') == poem_data.get('swedish_title'):
                existing_poems[i] = poem_data
                found = True
                break

        if not found:
            existing_poems.append(poem_data)

        # Write back
        with open(self.jsonl_path, 'w', encoding='utf-8') as f:
            for poem in existing_poems:
                f.write(json.dumps(poem, ensure_ascii=False) + '\n')

    def show_progress(self):
        """Show collection progress."""
        template_poems = self.load_template()
        collected_poems = self.load_existing_poems()

        print("\n" + "="*60)
        print("COLLECTION PROGRESS")
        print("="*60)
        print(f"Total poems identified: {len(template_poems)}")
        print(f"Poems collected: {len(collected_poems)}")
        print(f"Remaining: {len(template_poems) - len(collected_poems)}")

        if collected_poems:
            print("\nCollected poems:")
            for poem in collected_poems:
                if poem.get('swedish_text') and poem['swedish_text'] != "[To be filled]":
                    print(f"  ✓ {poem.get('swedish_title')} / {poem.get('english_title')}")

        print("\n")

    def get_next_uncollected_poem(self):
        """Get the next poem from template that hasn't been collected."""
        template_poems = self.load_template()
        collected_poems = self.load_existing_poems()

        collected_titles = {p.get('swedish_title') for p in collected_poems
                           if p.get('swedish_text') and p['swedish_text'] != "[To be filled]"}

        for poem in template_poems:
            if poem.get('swedish_title') not in collected_titles:
                return poem

        return None

    def collect_poem_interactive(self, poem_metadata=None):
        """Interactive poem collection."""
        if poem_metadata:
            print("\n" + "="*60)
            print(f"Collecting: {poem_metadata.get('swedish_title')}")
            print(f"English: {poem_metadata.get('english_title')}")
            print(f"Collection: {poem_metadata.get('collection')} ({poem_metadata.get('year')})")
            print(f"Translator: {poem_metadata.get('translator')}")
            print("\nSources:")
            print(f"  Swedish: {poem_metadata.get('source_swedish')}")
            print(f"  English: {poem_metadata.get('source_english')}")
            print("="*60 + "\n")
        else:
            poem_metadata = {}
            print("\n" + "="*60)
            print("Enter poem metadata:")
            print("="*60)
            poem_metadata['swedish_title'] = input("Swedish title: ").strip()
            poem_metadata['english_title'] = input("English title: ").strip()
            poem_metadata['collection'] = input("Collection (optional): ").strip()
            poem_metadata['year'] = input("Year (optional): ").strip()
            poem_metadata['translator'] = input("Translator (optional): ").strip()

        print("\nPaste the SWEDISH poem text below.")
        print("(Press Ctrl+D on a new line when done, or type '###END###' on a new line)")
        print("-" * 60)

        swedish_lines = []
        try:
            while True:
                line = input()
                if line.strip() == '###END###':
                    break
                swedish_lines.append(line)
        except EOFError:
            pass

        swedish_text = '\n'.join(swedish_lines).strip()

        if not swedish_text:
            print("No Swedish text entered. Skipping.")
            return False

        print("\n" + "-" * 60)
        print("Paste the ENGLISH translation below.")
        print("(Press Ctrl+D on a new line when done, or type '###END###' on a new line)")
        print("-" * 60)

        english_lines = []
        try:
            while True:
                line = input()
                if line.strip() == '###END###':
                    break
                english_lines.append(line)
        except EOFError:
            pass

        english_text = '\n'.join(english_lines).strip()

        if not english_text:
            print("No English text entered. Skipping.")
            return False

        # Get next poem number and save
        poem_num = self.get_next_poem_number()
        swedish_file, english_file = self.save_poem_files(poem_num, swedish_text, english_text)

        # Update metadata
        poem_metadata['swedish_text'] = swedish_text
        poem_metadata['english_text'] = english_text
        poem_metadata['poem_number'] = poem_num
        poem_metadata['collected_date'] = datetime.now().isoformat()
        poem_metadata['swedish_file'] = str(swedish_file)
        poem_metadata['english_file'] = str(english_file)

        # Save to JSONL
        self.update_jsonl(poem_metadata)

        print("\n" + "="*60)
        print(f"✓ Successfully saved poem #{poem_num}!")
        print(f"  Swedish: {swedish_file}")
        print(f"  English: {english_file}")
        print("="*60 + "\n")

        return True

    def run_interactive_session(self):
        """Run interactive collection session."""
        print("\n" + "="*60)
        print("GUSTAF FRÖDING POEM COLLECTOR")
        print("="*60)
        print("\nThis tool helps you manually collect poems from websites")
        print("and saves them in the format: poemN-swedish.txt, poemN-english.txt\n")

        self.show_progress()

        while True:
            next_poem = self.get_next_uncollected_poem()

            if next_poem:
                print(f"\nNext uncollected poem: {next_poem.get('swedish_title')}")
                response = input("Collect this poem? (y/n/q to quit): ").strip().lower()

                if response == 'q':
                    break
                elif response == 'y':
                    self.collect_poem_interactive(next_poem)
                else:
                    response = input("Skip and collect a different poem? (y/n): ").strip().lower()
                    if response == 'y':
                        self.collect_poem_interactive()
                    elif response == 'n':
                        break
            else:
                print("\nNo more poems in template.")
                response = input("Add a new poem not in template? (y/n): ").strip().lower()
                if response == 'y':
                    self.collect_poem_interactive()
                else:
                    break

            response = input("\nContinue collecting more poems? (y/n): ").strip().lower()
            if response != 'y':
                break

        print("\n" + "="*60)
        print("FINAL PROGRESS")
        self.show_progress()
        print("Thank you for collecting Gustaf Fröding poems!")
        print("="*60 + "\n")

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Manual poem collection helper')
    parser.add_argument('--output-dir', default='poems/froding', help='Output directory for poem files')
    parser.add_argument('--resume', action='store_true', help='Resume collection session')
    parser.add_argument('--stats', action='store_true', help='Show statistics only')

    args = parser.parse_args()

    collector = PoemCollector(output_dir=args.output_dir)

    if args.stats:
        collector.show_progress()
    else:
        collector.run_interactive_session()

if __name__ == '__main__':
    main()
