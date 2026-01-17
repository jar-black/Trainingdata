#!/usr/bin/env python3
"""
Script to help collect and format Gustaf Fröding poems with Swedish-English pairs.

This script provides utilities to:
1. Parse poem texts from various sources
2. Validate poem pairs have both Swedish and English versions
3. Format data as JSONL for training
4. Generate statistics about the collection

Usage:
    python collect_froding_poems.py --help
"""

import json
import argparse
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict


@dataclass
class Poem:
    """Data structure for a Gustaf Fröding poem with translation."""
    swedish_title: str
    english_title: str
    swedish_text: str
    english_text: str
    collection: str
    year: int
    translator: str
    source_swedish: str
    source_english: str

    def is_complete(self) -> bool:
        """Check if all required fields are filled."""
        return (
            self.swedish_text and
            self.english_text and
            not self.swedish_text.startswith("[To be filled") and
            not self.english_text.startswith("[To be filled")
        )

    def to_dict(self) -> Dict:
        """Convert to dictionary."""
        return asdict(self)


class FrodingCollection:
    """Manages the collection of Fröding poems."""

    def __init__(self, data_path: str = "data/froding_poems.jsonl"):
        self.data_path = Path(data_path)
        self.poems: List[Poem] = []

    def load_poems(self) -> int:
        """Load poems from JSONL file."""
        if not self.data_path.exists():
            print(f"File not found: {self.data_path}")
            return 0

        count = 0
        with open(self.data_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    data = json.loads(line)
                    poem = Poem(**data)
                    self.poems.append(poem)
                    count += 1
        return count

    def save_poems(self, output_path: Optional[str] = None) -> int:
        """Save poems to JSONL file."""
        path = Path(output_path) if output_path else self.data_path
        path.parent.mkdir(parents=True, exist_ok=True)

        count = 0
        with open(path, 'w', encoding='utf-8') as f:
            for poem in self.poems:
                json_line = json.dumps(poem.to_dict(), ensure_ascii=False)
                f.write(json_line + '\n')
                count += 1
        return count

    def add_poem(self, poem: Poem) -> None:
        """Add a poem to the collection."""
        self.poems.append(poem)

    def get_statistics(self) -> Dict:
        """Get statistics about the collection."""
        total = len(self.poems)
        complete = sum(1 for p in self.poems if p.is_complete())
        incomplete = total - complete

        collections = {}
        translators = {}
        years = {}

        for poem in self.poems:
            collections[poem.collection] = collections.get(poem.collection, 0) + 1
            translators[poem.translator] = translators.get(poem.translator, 0) + 1
            if isinstance(poem.year, int):
                years[poem.year] = years.get(poem.year, 0) + 1

        return {
            'total_poems': total,
            'complete_poems': complete,
            'incomplete_poems': incomplete,
            'collections': collections,
            'translators': translators,
            'years': years
        }

    def print_statistics(self) -> None:
        """Print collection statistics."""
        stats = self.get_statistics()

        print("\n=== Gustaf Fröding Poem Collection Statistics ===\n")
        print(f"Total poems: {stats['total_poems']}")
        print(f"Complete poems (both Swedish & English): {stats['complete_poems']}")
        print(f"Incomplete poems: {stats['incomplete_poems']}")

        print("\n--- By Collection ---")
        for collection, count in sorted(stats['collections'].items()):
            print(f"  {collection}: {count}")

        print("\n--- By Translator ---")
        for translator, count in sorted(stats['translators'].items()):
            print(f"  {translator}: {count}")

        print("\n--- By Year ---")
        for year, count in sorted(stats['years'].items()):
            print(f"  {year}: {count}")
        print()

    def list_incomplete(self) -> None:
        """List all incomplete poems."""
        incomplete = [p for p in self.poems if not p.is_complete()]

        if not incomplete:
            print("All poems are complete!")
            return

        print(f"\n=== Incomplete Poems ({len(incomplete)}) ===\n")
        for i, poem in enumerate(incomplete, 1):
            print(f"{i}. {poem.swedish_title} / {poem.english_title}")
            if poem.swedish_text.startswith("[To be filled"):
                print("   Missing: Swedish text")
            if poem.english_text.startswith("[To be filled"):
                print("   Missing: English text")
        print()

    def export_for_training(self, output_path: str) -> int:
        """
        Export complete poems in training format.
        Creates conversation pairs for translation training.
        """
        complete_poems = [p for p in self.poems if p.is_complete()]

        training_data = []
        for poem in complete_poems:
            # Swedish to English translation
            training_data.append({
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a translator specializing in Swedish poetry. Translate the following poem by Gustaf Fröding from Swedish to English, preserving the poetic style and meter."
                    },
                    {
                        "role": "user",
                        "content": f"Title: {poem.swedish_title}\n\n{poem.swedish_text}"
                    },
                    {
                        "role": "assistant",
                        "content": f"Title: {poem.english_title}\n\n{poem.english_text}"
                    }
                ],
                "metadata": {
                    "collection": poem.collection,
                    "year": poem.year,
                    "translator": poem.translator
                }
            })

            # English to Swedish translation (reverse)
            training_data.append({
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a translator specializing in Swedish poetry. Translate the following poem by Gustaf Fröding from English to Swedish, preserving the poetic style and meter."
                    },
                    {
                        "role": "user",
                        "content": f"Title: {poem.english_title}\n\n{poem.english_text}"
                    },
                    {
                        "role": "assistant",
                        "content": f"Title: {poem.swedish_title}\n\n{poem.swedish_text}"
                    }
                ],
                "metadata": {
                    "collection": poem.collection,
                    "year": poem.year,
                    "translator": poem.translator
                }
            })

        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)

        with open(output, 'w', encoding='utf-8') as f:
            for item in training_data:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')

        return len(training_data)


def main():
    parser = argparse.ArgumentParser(
        description="Manage Gustaf Fröding poem collection"
    )
    parser.add_argument(
        '--input',
        default='data/froding_poems_template.jsonl',
        help='Input JSONL file with poems'
    )
    parser.add_argument(
        '--stats',
        action='store_true',
        help='Show collection statistics'
    )
    parser.add_argument(
        '--list-incomplete',
        action='store_true',
        help='List incomplete poems'
    )
    parser.add_argument(
        '--export-training',
        type=str,
        help='Export complete poems to training format (specify output path)'
    )

    args = parser.parse_args()

    collection = FrodingCollection(args.input)
    loaded = collection.load_poems()
    print(f"Loaded {loaded} poems from {args.input}")

    if args.stats:
        collection.print_statistics()

    if args.list_incomplete:
        collection.list_incomplete()

    if args.export_training:
        count = collection.export_for_training(args.export_training)
        print(f"\nExported {count} training examples to {args.export_training}")


if __name__ == '__main__':
    main()
