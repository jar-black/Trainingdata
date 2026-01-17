# Gustaf Fröding Poems Collection - Summary Report

## Overview

This report summarizes the research and setup for collecting Gustaf Fröding poems with both Swedish originals and English translations for use as training data.

## What Was Accomplished

### 1. Research & Source Identification

I conducted extensive research and identified comprehensive sources for Gustaf Fröding poems:

**16 poem pairs identified** with confirmed Swedish and English versions available:
- 9 poems from "Gitarr och dragharmonika" (1891)
- 2 poems from "Nya dikter" (1894)
- 2 poems from "Stänk och flikar" (1896)
- 1 poem from "Gralstänk" (1898)
- 2 poems from various collections

**Potential for 30+ poems total** - The "Anthology of Swedish Lyrics" contains 37 Fröding poems in English translation.

### 2. Files Created

#### Data Files
- **`/home/user/Trainingdata/data/froding_poems_template.jsonl`**
  - Pre-populated with 16 known poem pairs
  - Structured format ready for filling in poem texts
  - Includes metadata (collection, year, translator, source URLs)

#### Documentation
- **`/home/user/Trainingdata/FRODING_COLLECTION_GUIDE.md`**
  - Comprehensive guide with all source URLs
  - Detailed list of identified poems
  - Collection strategies and copyright information

- **`/home/user/Trainingdata/FRODING_SUMMARY.md`** (this file)
  - Project overview and summary

#### Scripts
- **`/home/user/Trainingdata/scripts/collect_froding_poems.py`**
  - Python utility to manage poem collection
  - View statistics, list incomplete poems
  - Export to training format when complete
  - Usage: `python3 scripts/collect_froding_poems.py --stats`

- **`/home/user/Trainingdata/scripts/scrape_froding_poems.py`**
  - Web scraper for automated collection
  - Supports allmogens.se and runeberg.org
  - Respects robots.txt and adds delays
  - May require HTML selector updates

- **`/home/user/Trainingdata/scripts/download_archive_resources.sh`**
  - Bash script to download resources from Archive.org
  - Downloads 6 key resources (text and PDF)
  - Public domain materials
  - Usage: `./scripts/download_archive_resources.sh`

## Key Sources Identified

### English Translations

1. **Charles Wharton Stork - "Selected Poems" (1916)**
   - Internet Archive: https://archive.org/details/selectedpoems00frodiala
   - Public domain, freely downloadable
   - Contains poems from multiple collections

2. **Charles Wharton Stork - "Anthology of Swedish Lyrics" (1917)**
   - 37 Fröding poems (most represented poet)
   - Internet Archive: https://archive.org/details/anthologyofswedi00stor
   - PDF: https://upload.wikimedia.org/wikipedia/commons/6/64/Anthology_of_Swedish_lyrics_from_1750_to_1915;_(IA_cu31924026327076).pdf

3. **Modern Web Resources**
   - Allmogens.se: 5 poems with English translations
   - LyricsTranslate.com: 3 poems with English translations

### Swedish Originals

1. **Project Runeberg**
   - Gitarr och dragharmonika: https://runeberg.org/dragharm/
   - Stänk och flikar: https://runeberg.org/stanflik/
   - Public domain digital library

2. **Litteraturbanken (Swedish Literature Bank)**
   - Professional digital editions
   - Available on Archive.org
   - EPUB and PDF formats

3. **Svenska Dikter & Svensk-poesi.com**
   - Individual poems available online
   - Modern websites with Swedish texts

## Identified Poems (16 confirmed pairs)

### From Gitarr och dragharmonika (1891)
1. Gitarr och dragharmonika / Guitar and Concertina
2. En hög visa / A Song-Of-Songs
3. Vackert väder / Lovely Weather
4. Indianer / Indians
5. Vallarelåt / Pastoral
6. Skogsrån / The Wood Sprite
7. Våran prost / Our Dean
8. Äktenskapsfrågan / Matrimonial Queries
9. Det var dans bort i vägen / The Ball

### From Nya dikter (1894)
10. Idealism och realism / Idealism and Realism
11. Den gamla goda tiden / The Good Old Days

### From Stänk och flikar (1896)
12. I ungdomen / In Youth
13. Strövtåg i hembygden / A Stroll Through the Local Countryside

### From Gralstänk (1898)
14. Friheten / Freedom

### From Various Collections
15. En kärleksvisa / A Ditty About Love
16. Säv, säv, susa / Rush, Rush, Whisper

## Why Direct Collection Failed

During my research, I encountered consistent 403 (Forbidden) errors when attempting to fetch content directly from websites, including:
- Project Runeberg
- Internet Archive text files
- Wikisource
- Swedish poetry websites
- Project Gutenberg

This appears to be due to network restrictions in the current environment that prevent automated web scraping and content fetching.

## Next Steps for Manual Collection

### Option 1: Download Archive.org Resources (Recommended)

1. Run the download script:
   ```bash
   ./scripts/download_archive_resources.sh
   ```

2. The script will download 6 resources to `downloads/archive_org/`:
   - Anthology of Swedish Lyrics (text and PDF)
   - Selected Poems (text)
   - Gitarr och dragharmonika (PDF)
   - Other supporting materials

3. Extract poem texts from the downloaded files

4. Populate the template file with actual poem texts

### Option 2: Manual Web Collection

1. Visit each source URL listed in `FRODING_COLLECTION_GUIDE.md`
2. Copy Swedish text from Project Runeberg or other Swedish sources
3. Copy English translation from corresponding English source
4. Paste into `data/froding_poems_template.jsonl`

### Option 3: Use the Web Scraper

1. Install dependencies:
   ```bash
   pip install requests beautifulsoup4
   ```

2. Try the scraper (may still encounter 403 errors):
   ```bash
   python3 scripts/scrape_froding_poems.py --source allmogens --output data/froding_poems.jsonl
   ```

3. Note: You may need to update HTML selectors in the code

## Using the Collection Tools

### Check Progress
```bash
python3 scripts/collect_froding_poems.py --input data/froding_poems_template.jsonl --stats
```

### List Incomplete Poems
```bash
python3 scripts/collect_froding_poems.py --input data/froding_poems_template.jsonl --list-incomplete
```

### Export to Training Format (when complete)
```bash
python3 scripts/collect_froding_poems.py --input data/froding_poems.jsonl --export-training data/froding_training.jsonl
```

This will create conversation-formatted training data with:
- Swedish → English translation examples
- English → Swedish translation examples
- Metadata about collection, year, and translator

## Training Data Format

Once complete, the poems can be exported to a training format suitable for instruction-tuning LLMs, similar to the existing `age_prediction_dataset.jsonl` in this repository.

Each poem generates 2 training examples:
- One for Swedish → English translation
- One for English → Swedish translation

## Copyright & Public Domain

- Gustaf Fröding's works: **Public Domain** (died 1911)
- Charles Wharton Stork translations (1916-1917): **Public Domain in USA**
- Modern translations: Check individual sources for licensing
- All Archive.org resources listed: **Public Domain**

## Estimated Collection Effort

- **Minimum viable dataset**: 10-15 poem pairs (already identified)
- **Good dataset**: 20-30 poem pairs (achievable with Anthology)
- **Comprehensive dataset**: 37+ poems (maximum from identified sources)

**Time estimate**:
- Manual collection: 30-60 minutes per poem (finding, copying, formatting)
- Total for 15 poems: 8-15 hours
- Using downloaded Archive.org files: Could be faster with PDF text extraction

## References

All detailed source URLs are in `FRODING_COLLECTION_GUIDE.md`.

Key sources:
- [Internet Archive - Selected Poems](https://archive.org/details/selectedpoems00frodiala)
- [Internet Archive - Anthology of Swedish Lyrics](https://archive.org/details/anthologyofswedi00stor)
- [Project Runeberg - Gitarr och dragharmonika](https://runeberg.org/dragharm/)
- [Allmogens.se - Gustaf Fröding](https://allmogens.se/en/poetry/)
- [Gustaf Fröding - Wikipedia](https://en.wikipedia.org/wiki/Gustaf_Fr%C3%B6ding)

## Questions or Issues?

If you encounter problems:
1. Check that source URLs are still accessible
2. Try downloading Archive.org resources directly in a web browser
3. Consider using the PDF versions and extracting text with tools like `pdftotext`
4. Verify robots.txt and terms of service for any automated collection

---

**Created**: 2026-01-17
**Status**: Research complete, ready for manual poem collection
**Dataset**: 16 poems identified, 0 complete (template created)
