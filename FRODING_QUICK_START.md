# Gustaf Fröding Poems - Quick Start Guide

## What's Ready

I've identified **16 poem pairs** with both Swedish and English versions available:

1. Gitarr och dragharmonika / Guitar and Concertina
2. En hög visa / A Song-Of-Songs
3. Vackert väder / Lovely Weather
4. Indianer / Indians
5. Vallarelåt / Pastoral
6. Skogsrån / The Wood Sprite
7. Våran prost / Our Dean
8. Äktenskapsfrågan / Matrimonial Queries
9. Det var dans bort i vägen / The Ball
10. I ungdomen / In Youth
11. Idealism och realism / Idealism and Realism
12. Den gamla goda tiden / The Good Old Days
13. Strövtåg i hembygden / A Stroll Through the Local Countryside
14. Friheten / Freedom
15. En kärleksvisa / A Ditty About Love
16. Säv, säv, susa / Rush, Rush, Whisper

**Potential**: Up to 37 poems total (from Anthology of Swedish Lyrics)

## Fastest Path to Collection

### Option A: Download from Archive.org (Recommended)

```bash
cd /home/user/Trainingdata
./scripts/download_archive_resources.sh
```

This downloads 6 public domain resources including:
- Anthology of Swedish Lyrics (37 Fröding poems in English)
- Selected Poems (1916) by Stork
- Swedish originals from Litteraturbanken

### Option B: Manual Collection from Websites

Visit the sources and copy-paste:

**Swedish Sources:**
- Project Runeberg: https://runeberg.org/dragharm/
- Litteraturbanken: https://litteraturbanken.se/

**English Sources:**
- Archive.org: https://archive.org/details/selectedpoems00frodiala
- Allmogens.se: https://allmogens.se/en/poetry/

### Option C: Try Web Scraping (May Fail)

```bash
pip install requests beautifulsoup4
python3 scripts/scrape_froding_poems.py --source allmogens --output data/froding_poems.jsonl
```

Note: Many sites block automated access (403 errors).

## Working with the Data

### Check Your Progress

```bash
python3 scripts/collect_froding_poems.py --input data/froding_poems_template.jsonl --stats
```

### See What's Missing

```bash
python3 scripts/collect_froding_poems.py --input data/froding_poems_template.jsonl --list-incomplete
```

### Export to Training Format

Once you've filled in the poem texts:

```bash
python3 scripts/collect_froding_poems.py \
  --input data/froding_poems.jsonl \
  --export-training data/froding_training.jsonl
```

This creates conversation-formatted training data for Swedish-English poetry translation.

## Data Format

Edit `data/froding_poems_template.jsonl` - each line is a JSON object:

```json
{
  "swedish_title": "Indianer",
  "english_title": "Indians",
  "swedish_text": "[Paste Swedish poem here]",
  "english_text": "[Paste English translation here]",
  "collection": "Gitarr och dragharmonika",
  "year": 1891,
  "translator": "Charles Wharton Stork",
  "source_swedish": "https://runeberg.org/dragharm/",
  "source_english": "Archive.org - Selected Poems (1916)"
}
```

## Key Sources

**English Translations:**
- Charles Wharton Stork's "Selected Poems" (1916) - Archive.org
- "Anthology of Swedish Lyrics" (1917) - 37 poems - Archive.org
- Allmogens.se - 5 poems with modern translations
- LyricsTranslate.com - 3 poems

**Swedish Originals:**
- Project Runeberg - Gitarr och dragharmonika, Stänk och flikar
- Litteraturbanken - Digital editions on Archive.org
- Svenska Dikter, Svensk-poesi.com

## Next Steps

1. **Read** `FRODING_COLLECTION_GUIDE.md` for detailed information
2. **Download** resources using the script or manually
3. **Extract** poem texts from downloaded files
4. **Populate** the template JSONL with actual texts
5. **Export** to training format

## Copyright

All identified sources are **public domain**:
- Fröding died in 1911 (public domain)
- Stork's translations from 1916-1917 (public domain in USA)
- Archive.org materials are freely available

## Questions?

See `FRODING_SUMMARY.md` for the full research report.
See `FRODING_COLLECTION_GUIDE.md` for comprehensive source documentation.

---

**Goal**: Collect 10-15 poem pairs minimum, 30+ poems ideally
**Format**: JSONL with Swedish-English pairs for translation training
**Status**: Infrastructure ready, awaiting poem text collection
