# Gustaf Fröding Poems Collection

This directory contains Gustaf Fröding's poems in paired Swedish-English format.

## File Format

Each poem is stored as a pair of files:
- `poem1-swedish.txt` - Swedish original
- `poem1-english.txt` - English translation
- `poem2-swedish.txt` - Swedish original
- `poem2-english.txt` - English translation
- ...and so on

## How to Collect Poems

### Method 1: Interactive Python Script (Recommended)

Run the manual collection helper:

```bash
cd /home/user/Trainingdata
python3 scripts/manual_poem_collector.py
```

This script will:
1. Guide you through collecting poems from the template
2. Prompt you to paste Swedish and English texts
3. Automatically number and save the files
4. Track your progress
5. Update the JSONL database

### Method 2: Manual File Creation

1. Visit the source websites:
   - **Swedish**: https://runeberg.org/dragharm/ or https://litteraturbanken.se/
   - **English**: https://allmogens.se/en/poetry/ or search for "Gustaf Fröding poems English translation"

2. Copy poem text from website

3. Create files manually:
   ```bash
   # Example for poem 1
   echo "Swedish poem text here" > poems/froding/poem1-swedish.txt
   echo "English translation here" > poems/froding/poem1-english.txt
   ```

## Poem Collection Guide

### 16 Known Poem Pairs with Translations

1. **Gitarr och dragharmonika** / Guitar and Concertina
   - Swedish: https://runeberg.org/dragharm/dragharm.html
   - English: Archive.org - Selected Poems (1916)

2. **Indianer** / Indians
   - Swedish: https://runeberg.org/dragharm/
   - English: Archive.org - Selected Poems (1916)

3. **Skogsrån** / The Wood Sprite
   - Swedish: https://runeberg.org/dragharm/
   - English: Archive.org - Selected Poems (1916)

4. **Vallarelåt** / Pastoral
   - Swedish: https://runeberg.org/dragharm/
   - English: Archive.org - Selected Poems (1916)

5. **Våran prost** / Our Dean
   - Swedish: https://runeberg.org/dragharm/
   - English: Archive.org - Selected Poems (1916)

6. **Äktenskapsfrågan** / Matrimonial Queries
   - Swedish: https://runeberg.org/dragharm/aktfraga.html
   - English: Archive.org - Selected Poems (1916)

7. **Det var dans bort i vägen** / The Ball
   - Swedish: https://runeberg.org/dragharm/
   - English: Archive.org - Selected Poems (1916)

8. **En hög visa** / A Song-Of-Songs
   - Swedish: https://runeberg.org/dragharm/
   - English: Archive.org - Selected Poems (1916)

9. **Vackert väder** / Lovely Weather
   - Swedish: https://runeberg.org/dragharm/
   - English: https://lyricstranslate.com/en/vackert-vader-lovely-weather.html

10. **I ungdomen** / In Youth
    - Swedish: https://runeberg.org/stanflik/
    - English: https://allmogens.se/en/poetry/i-ungdomen/

11. **Idealism och realism** / Idealism and Realism
    - Swedish: Various sources
    - English: https://allmogens.se/en/poetry/idealism-och-realism/

12. **Friheten** / Freedom
    - Swedish: Various sources
    - English: https://allmogens.se/en/poetry/friheten/

13. **Den gamla goda tiden** / The Good Old Days
    - Swedish: Various sources
    - English: https://allmogens.se/en/poetry/den-gamla-goda-tiden/

14. **Strövtåg i hembygden** / A Stroll Through the Local Countryside
    - Swedish: https://runeberg.org/stanflik/09.html
    - English: https://allmogens.se/en/poetry/strovtag-i-hembygden/

15. **En kärleksvisa** / A Ditty About Love
    - Swedish: https://lyricstranslate.com/
    - English: https://lyricstranslate.com/en/en-k%C3%A4rleksvisa-ditty-about-love.html

16. **Säv, säv, susa** / Rush, Rush, Whisper
    - Swedish: https://lyricstranslate.com/
    - English: https://lyricstranslate.com/en/sav-sav-susa-rush-rush-whisper.html-0

## Key Sources

### English Translations

1. **Charles Wharton Stork - Selected Poems (1916)**
   - Archive.org: https://archive.org/details/selectedpoems00frodiala
   - Contains many Fröding poems translated to English
   - Public domain

2. **Anthology of Swedish Lyrics (1917)**
   - Archive.org: https://archive.org/details/anthologyofswedi00stor
   - Contains 37 Fröding poems in English
   - Public domain

3. **Allmogens.se**
   - https://allmogens.se/en/poetry/
   - 5 poems with modern English translations
   - Freely accessible

4. **LyricsTranslate.com**
   - https://lyricstranslate.com/
   - 3 poems with English translations
   - Community-contributed

### Swedish Originals

1. **Project Runeberg**
   - Gitarr och dragharmonika: https://runeberg.org/dragharm/
   - Stänk och flikar: https://runeberg.org/stanflik/
   - Full text of original collections
   - Public domain

2. **Litteraturbanken**
   - https://litteraturbanken.se/
   - Swedish literature archive
   - Digital editions

3. **Wikisource (Swedish)**
   - https://sv.wikisource.org/
   - Various Fröding poems

## Tips for Collection

1. **Start with Allmogens.se** - It has 5 poems with both Swedish and English readily available

2. **Use Archive.org** - Download the PDF or text versions of Stork's translations (though automated access may be blocked)

3. **Use the Python script** - It tracks your progress and prevents duplicates

4. **Check your progress**:
   ```bash
   python3 scripts/manual_poem_collector.py --stats
   ```

5. **Verify file count**:
   ```bash
   ls poems/froding/*.txt | wc -l
   # Should be even number (pairs of Swedish/English)
   ```

## Copyright Status

All materials are **public domain**:
- Gustaf Fröding died in 1911 (works entered public domain)
- Charles Wharton Stork's translations from 1916-1917 (public domain in USA)
- Archive.org resources are freely available

## Goal

Collect at least 10-15 poem pairs initially, with potential for 30+ poems total (based on Anthology of Swedish Lyrics content).

## Questions?

See the main repository documentation:
- `FRODING_QUICK_START.md` - Quick start guide
- `FRODING_COLLECTION_GUIDE.md` - Comprehensive source list
- `FRODING_SUMMARY.md` - Full research report
