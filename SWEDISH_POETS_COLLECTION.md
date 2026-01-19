# Swedish Poets Collection - Project Summary

This project contains Swedish-English poem pairs from 5 major Swedish poets, all in public domain.

## Collection Status

| Poet | Years | Poems Identified | Poems Collected | Status |
|------|-------|------------------|-----------------|--------|
| **Gustaf Fröding** | 1860-1911 | 16 | 0 | Infrastructure ready |
| **Verner von Heidenstam** | 1859-1940 | 30 | **30** ✓ | **COMPLETE** |
| **Erik Axel Karlfeldt** | 1864-1931 | 30 | 0 | Infrastructure ready |
| **Viktor Rydberg** | 1828-1895 | 22 | 0 | Infrastructure ready |
| **Esaias Tegnér** | 1782-1846 | ~15 | 0 | Infrastructure ready |
| **TOTAL** | | **~113** | **30** | **26% Complete** |

## What Was Created

### 1. Complete Infrastructure for 5 Swedish Poets

Each poet has:
- `poems/{poet}/` directory for poem files
- `poems/{poet}/README.md` with sources and instructions
- `data/{poet}_poems_template.jsonl` with poem metadata
- `scripts/collect_{poet}_poems.py` collection helper (most poets)

### 2. Actual Collected Poems

**Verner von Heidenstam: 30 poem pairs (60 files)**
- All from "Sweden's Laureate: Selected Poems" (1919) translated by Charles Wharton Stork
- Covers his major collections from 1888-1915
- Files: `poems/heidenstam/poem1-swedish.txt`, `poem1-english.txt`, etc.

### 3. Documentation

- `SWEDISH_POETS_COLLECTION.md` - This summary document
- `FRODING_COLLECTION_GUIDE.md` - Comprehensive Fröding sources
- `FRODING_QUICK_START.md` - Quick start for Fröding
- `FRODING_SUMMARY.md` - Detailed Fröding research
- `KARLFELDT_COLLECTION_SUMMARY.md` - Karlfeldt overview
- `RYDBERG_COLLECTION_GUIDE.md` - Rydberg quick start
- `RYDBERG_SUMMARY.md` - Rydberg detailed research

## File Format

All poems follow consistent naming:
- Swedish: `poem1-swedish.txt`, `poem2-swedish.txt`, etc.
- English: `poem1-english.txt`, `poem2-english.txt`, etc.

## Key Public Domain Sources

### Primary English Translation Source

**"Anthology of Swedish Lyrics from 1750 to 1915"** (1917)
- Translated by Charles Wharton Stork
- Contains poems from all 5 poets:
  - Fröding: 37 poems
  - Heidenstam: 27 poems
  - Karlfeldt: 27 poems
  - Rydberg: 22 poems
  - Tegnér: 13 poems
- Archive.org: https://archive.org/details/anthologyofswedi00stor
- Public domain in USA (published 1917)

### Additional English Sources

1. **Heidenstam**: "Sweden's Laureate" (1919) - Charles Wharton Stork
2. **Karlfeldt**: "Arcadia Borealis" (1938) - Charles Wharton Stork
3. **Tegnér**: "Poems by Tegnér" - Longfellow & Blackley translations
4. **Fröding**: "Selected Poems" (1916) - Charles Wharton Stork

### Swedish Originals

**Projekt Runeberg** - http://runeberg.org/
- Complete digital editions of all Swedish poetry collections
- All public domain (poets died 1846-1940)

**Swedish Wikisource** - https://sv.wikisource.org/
- Individual poems and collections

## Copyright Status

✓ **All materials are PUBLIC DOMAIN**
- All poets died before 1945 (works in public domain worldwide)
- English translations from 1917-1938 (public domain in USA)
- Swedish originals freely available on Projekt Runeberg

## Next Steps for Collection

### Priority 1: Complete Remaining Fröding Poems
- 16 poems identified, sources documented
- Use: `python3 scripts/manual_poem_collector.py`

### Priority 2: Collect Karlfeldt Poems
- 30 poems identified from Anthology + Arcadia Borealis
- Use: `python3 scripts/collect_karlfeldt_poems.py`

### Priority 3: Collect Rydberg Poems
- 22 poems from Anthology of Swedish Lyrics
- Use: `python3 scripts/collect_rydberg_poems.py`

### Priority 4: Collect Tegnér Poems
- ~15 poems from various sources
- Use: `python3 scripts/collect_tegner_poems.py`

## Manual Collection Workflow

1. **Visit Archive.org** with a free account
2. **Download/view** the anthology or specific collection
3. **Copy poem text** (Swedish from Runeberg, English from Archive.org)
4. **Use collection script** to save and track progress
5. **Files auto-named** as poemN-swedish.txt, poemN-english.txt

## Why Manual Collection?

Automated web scraping encountered 403 errors on all major sources:
- Archive.org
- Projekt Runeberg
- Wikisource
- Poetry websites

However, all sources are freely accessible with manual browser access.

## About the Poets

### Gustaf Fröding (1860-1911)
- Major Swedish poet from Värmland
- Nobel Prize consideration
- Collections: Gitarr och dragharmonika (1891), Nya dikter (1894)

### Verner von Heidenstam (1859-1940)
- Nobel Prize in Literature 1916
- Collections: Vallfart och vandringsår (1888), Dikter (1895)
- Major themes: Swedish nationalism, romanticism

### Erik Axel Karlfeldt (1864-1931)
- Nobel Prize in Literature 1931 (posthumously)
- Collections: Flora och Pomona (1906), Hösthorn (1927)
- Regional poet from Dalarna

### Viktor Rydberg (1828-1895)
- Philosopher, poet, novelist
- Famous for "Tomten" (The House-Goblin)
- Major influence on Swedish literature

### Esaias Tegnér (1782-1846)
- Bishop and Romantic poet
- "Frithiof's Saga" translated 22 times into English
- "The Children of the Lord's Supper" translated by Longfellow

## Technical Details

### Directory Structure
```
/home/user/Trainingdata/
├── poems/
│   ├── froding/         (16 poems planned)
│   ├── heidenstam/      (30 poems ✓ COLLECTED)
│   ├── karlfeldt/       (30 poems planned)
│   ├── rydberg/         (22 poems planned)
│   └── tegner/          (15 poems planned)
├── data/
│   ├── froding_poems_template.jsonl
│   ├── heidenstam_poems_template.jsonl
│   ├── karlfeldt_poems_template.jsonl
│   └── rydberg_poems_template.jsonl
└── scripts/
    ├── manual_poem_collector.py        (generic)
    ├── collect_froding_poems.py
    ├── collect_karlfeldt_poems.py
    ├── collect_rydberg_poems.py
    └── collect_tegner_poems.py
```

### JSONL Format
Each poem entry contains:
```json
{
  "swedish_title": "Title in Swedish",
  "english_title": "Title in English",
  "swedish_text": "Full Swedish poem text",
  "english_text": "Full English translation",
  "collection": "Collection name",
  "year": 1891,
  "translator": "Charles Wharton Stork",
  "source_swedish": "URL to Swedish original",
  "source_english": "URL to English translation"
}
```

## Usage for Training Data

These poem pairs are ideal for:
- Swedish-English translation model training
- Literary translation studies
- Evaluation of translation quality
- Cross-lingual poetry analysis
- Historical language modeling

## Estimated Time for Full Collection

- Heidenstam: ✓ Done (30 poems)
- Fröding: ~2-3 hours (16 poems)
- Karlfeldt: ~4-5 hours (30 poems)
- Rydberg: ~3-4 hours (22 poems)
- Tegnér: ~2-3 hours (15 poems)

**Total**: ~11-15 hours for complete collection of all 113 poems

## Notes

- All infrastructure is ready for immediate use
- Scripts include progress tracking and automatic file naming
- Sources are well-documented with direct URLs
- Copyright status verified for all materials
- Consistent file format across all poets
