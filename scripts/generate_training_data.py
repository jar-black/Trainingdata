#!/usr/bin/env python3
"""
Generate comprehensive training data from all available poems.
Creates examples at multiple granularities: full poems, stanzas, and lines.
"""

import json
import os
import re
from pathlib import Path

def read_poem(filepath):
    """Read a poem file and return its content."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read().strip()

def split_into_stanzas(text):
    """Split poem text into stanzas (separated by blank lines)."""
    # Split by one or more blank lines
    stanzas = re.split(r'\n\s*\n', text)
    return [s.strip() for s in stanzas if s.strip()]

def split_into_lines(text, min_lines=2, max_lines=4):
    """Split poem into multi-line chunks."""
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    chunks = []

    # Create chunks of 2-4 lines
    for size in range(min_lines, max_lines + 1):
        for i in range(len(lines) - size + 1):
            chunk = '\n'.join(lines[i:i+size])
            if chunk:
                chunks.append(chunk)

    return chunks

def get_poem_title(text):
    """Extract title from poem (first line or two)."""
    lines = text.split('\n')
    if len(lines) >= 2:
        return f"{lines[0]}\n{lines[1]}"
    return lines[0] if lines else ""

def generate_training_examples(english_file, swedish_file):
    """Generate training examples from a poem pair."""
    english_text = read_poem(english_file)
    swedish_text = read_poem(swedish_file)

    examples = []

    # Skip if either file is too short or empty
    if len(english_text) < 50 or len(swedish_text) < 50:
        return examples

    # 1. Full poem example
    examples.append({
        "instruction": "Translate the following English poem to Swedish.",
        "input": english_text,
        "output": swedish_text
    })

    # 2. Stanza-level examples
    eng_stanzas = split_into_stanzas(english_text)
    swe_stanzas = split_into_stanzas(swedish_text)

    if len(eng_stanzas) == len(swe_stanzas) and len(eng_stanzas) > 1:
        for eng_stanza, swe_stanza in zip(eng_stanzas, swe_stanzas):
            # Skip title stanzas (very short)
            if len(eng_stanza) > 30 and len(swe_stanza) > 30:
                examples.append({
                    "instruction": "Translate the following English poem to Swedish.",
                    "input": eng_stanza,
                    "output": swe_stanza
                })

    # 3. Multi-line excerpts (2-4 lines)
    # Only add these for longer poems to avoid too much duplication
    if len(english_text) > 200:
        eng_lines = split_into_lines(english_text, min_lines=2, max_lines=3)
        swe_lines = split_into_lines(swedish_text, min_lines=2, max_lines=3)

        # Add a sample of line pairs (not all to avoid data explosion)
        step = max(1, len(eng_lines) // 10)  # Take ~10 samples
        for eng_chunk, swe_chunk in zip(eng_lines[::step], swe_lines[::step]):
            if len(eng_chunk) > 20 and len(swe_chunk) > 20:
                examples.append({
                    "instruction": "Translate the following English text to Swedish.",
                    "input": eng_chunk,
                    "output": swe_chunk
                })

    return examples

def main():
    """Main function to generate all training data."""
    poems_dir = Path("/home/user/Trainingdata/poems")
    output_file = Path("/home/user/Trainingdata/data/english_to_swedish_poetry_translation.json")

    all_examples = []
    poem_count = 0

    # Process all poets
    for poet_dir in sorted(poems_dir.iterdir()):
        if not poet_dir.is_dir():
            continue

        poet_name = poet_dir.name
        print(f"Processing {poet_name}...")

        # Find all English poem files
        english_files = sorted(poet_dir.glob("*-english.txt"))

        for eng_file in english_files:
            # Get corresponding Swedish file
            swe_file = eng_file.parent / eng_file.name.replace("-english.txt", "-swedish.txt")

            if swe_file.exists():
                poem_id = eng_file.stem.replace("-english", "")
                print(f"  Processing {poem_id}...")

                examples = generate_training_examples(eng_file, swe_file)
                if examples:
                    all_examples.extend(examples)
                    poem_count += 1
                    print(f"    Added {len(examples)} examples")

    # Save to JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_examples, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"Total poems processed: {poem_count}")
    print(f"Total training examples: {len(all_examples)}")
    print(f"Output file: {output_file}")
    print(f"File size: {output_file.stat().st_size / 1024:.1f} KB")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
