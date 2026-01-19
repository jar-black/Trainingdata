#!/usr/bin/env python3
"""
Update tegner_poems.jsonl with actual poem texts from collected files.

This script reads the Swedish and English text files and updates the JSONL
file with the complete poem texts.

Usage:
    python3 scripts/update_tegner_jsonl.py
"""

import json
import os
from pathlib import Path

POEMS_DIR = Path("/home/user/Trainingdata/poems/tegner")
JSONL_FILE = Path("/home/user/Trainingdata/data/tegner_poems.jsonl")

def read_poem_file(filepath):
    """Read a poem text file and return its contents."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip()
            # Check if it's just a template
            if "[COLLECTION NEEDED]" in content:
                return None
            return content
    except FileNotFoundError:
        return None

def update_jsonl():
    """Update the JSONL file with poem texts from files."""
    # Read existing JSONL
    poems = []
    with open(JSONL_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            poems.append(json.loads(line))

    # Update with actual texts
    updated_count = 0
    for poem in poems:
        poem_id = poem['poem_id']
        swedish_file = POEMS_DIR / poem['swedish_file']
        english_file = POEMS_DIR / poem['english_file']

        # Read texts
        swedish_text = read_poem_file(swedish_file)
        english_text = read_poem_file(english_file)

        # Update poem entry
        if swedish_text:
            poem['swedish_text'] = swedish_text
            poem['collection_status'] = 'swedish_collected'
            updated_count += 1
        else:
            poem['swedish_text'] = ""

        if english_text:
            poem['english_text'] = english_text
            if swedish_text:
                poem['collection_status'] = 'complete'
            else:
                poem['collection_status'] = 'english_collected'
            updated_count += 1
        else:
            poem['english_text'] = ""

        if not swedish_text and not english_text:
            poem['collection_status'] = 'template_only'

    # Write updated JSONL
    with open(JSONL_FILE, 'w', encoding='utf-8') as f:
        for poem in poems:
            f.write(json.dumps(poem, ensure_ascii=False) + '\n')

    # Report statistics
    print(f"Updated {updated_count} poem texts")
    print("\nCollection Status:")
    status_counts = {}
    for poem in poems:
        status = poem.get('collection_status', 'unknown')
        status_counts[status] = status_counts.get(status, 0) + 1

    for status, count in sorted(status_counts.items()):
        print(f"  {status}: {count}")

    complete = status_counts.get('complete', 0)
    total = len(poems)
    print(f"\nCompletion: {complete}/{total} poem pairs ({100*complete/total:.1f}%)")

if __name__ == "__main__":
    update_jsonl()
