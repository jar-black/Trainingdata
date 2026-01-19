# Viktor Rydberg Poems Collection

This directory contains Viktor Rydberg's poems in paired Swedish-English format.

## About Viktor Rydberg (1828-1895)

Viktor Rydberg was one of Sweden's most important 19th-century authors, known for his philosophical poetry, novels, and mythological research. His works are in the public domain worldwide (died 1895).

## File Format

Each poem is stored as a pair of files:
- `poem1-swedish.txt` - Swedish original
- `poem1-english.txt` - English translation
- `poem2-swedish.txt` - Swedish original
- `poem2-english.txt` - English translation
- ...and so on

## 22 Poem Pairs Available

Based on Charles Wharton Stork's "Anthology of Swedish Lyrics from 1750 to 1915" (1917), which contains 22 Rydberg poems:

1. **Tomten** / The House-Goblin (1881)
   - His most famous poem, a Christmas favorite
   - Swedish: https://runeberg.org/rydbdikt/tomten.html

2. **De badande barnen** / The Bathing Children
   - Intimate picture of Swedish country life
   - Swedish: https://runeberg.org/rydbdikt/

3. **Den nya Grottesången** / The New Grotti Song
   - Social commentary on factory working conditions
   - Swedish: https://runeberg.org/rydbdikt/

4. **Dexippos** / Dexippus (1876)
   - Swedish: https://runeberg.org/rydbdikt/dexippos.html

5. **Skogsrået** / The Wood Nymph
   - Swedish: https://runeberg.org/rydbdikt/skogsr.html

6. **Snöfrid** / Snowfrid
   - Swedish: https://runeberg.org/rydbdikt/snofrid.html

7. **Korpen** / The Raven
   - Swedish: https://runeberg.org/rydbdikt/korpen.html

8. **Drömliv** / Dream Life
   - Swedish: https://runeberg.org/rydbdikt/dromliv.html

9. **På floden** / On the River
   - Swedish: https://runeberg.org/rydbdikt/pafloden.html

10. **Kantat** / Cantata
    - Swedish: https://runeberg.org/rydbdikt/kantat.html

11. **En blomma** / A Flower
    - Swedish: https://runeberg.org/rydbdikt/enblomma.html

12. **Höstkväll** / Autumn Evening
    - Swedish: https://runeberg.org/rydbdikt/hostkvall.html

13. **Den flygande holländaren** / The Flying Dutchman
    - Swedish: https://runeberg.org/rydbdikt/flygholl.html

14. **Prometeus och Ahasverus** / Prometheus and Ahasuerus
    - Swedish: https://runeberg.org/rydbdikt/prometas.html

15. **Till ödet** / To Fate
    - Swedish: https://runeberg.org/rydbdikt/tillodet.html

16. **Vaknen!** / Awaken!
    - Swedish: https://runeberg.org/rydbdikt/vaknen.html

17. **Drömmaren** / The Dreamer
    - Swedish: https://runeberg.org/rydbdikt/drommaren.html

18. **Vadan och varthän?** / Whence and Whither?
    - Swedish: https://runeberg.org/rydbdikt/vadanvar.html

19. **Älvan till flickan** / The Elf to the Maiden
    - Swedish: https://runeberg.org/rydbdikt/alvantil.html

20. **Baldersbålet** / Balder's Pyre
    - Swedish: https://runeberg.org/rydbdikt/balders.html

21. **Klockorna** / The Bells
    - Swedish: https://runeberg.org/rydbdikt/klockor.html

22. **Vinst och förlust** / Gain and Loss
    - Swedish: https://runeberg.org/rydbdikt/vinstfor.html

## Key Sources

### English Translations

1. **Charles Wharton Stork - Anthology of Swedish Lyrics (1917)**
   - Archive.org: https://archive.org/details/anthologyofswedi00stor
   - Alternative: https://archive.org/details/anthologyswedis00storgoog
   - Contains 22 Rydberg poems translated to English
   - Public domain (published 1917)
   - Full text: https://archive.org/stream/anthologyofswedi00stor/anthologyofswedi00stor_djvu.txt

2. **Wikimedia Commons PDF**
   - Direct PDF: https://upload.wikimedia.org/wikipedia/commons/6/64/Anthology_of_Swedish_lyrics_from_1750_to_1915;_(IA_cu31924026327076).pdf
   - Complete anthology in PDF format

3. **LyricsTranslate.com**
   - "Tomten" translations: https://lyricstranslate.com/en/tomten-tomten.html
   - Multiple English versions by different translators
   - Community-contributed

4. **Individual Poem Sites**
   - "Tomten": https://www.tomtenposter.com/Tomten.html
   - Various other poems on poetry sites

### Swedish Originals

1. **Project Runeberg - Dikter av Viktor Rydberg**
   - Main collection: https://runeberg.org/rydbdikt/
   - Complete works: https://runeberg.org/authors/rydberg.html
   - Full text of Rydberg's collected poems ("Dikter")
   - Public domain
   - Archive.org mirror: https://archive.org/stream/arkivkopia.se-runeberg-rydbdikt/rydbdikt_djvu.txt

2. **Svenska Dikter**
   - https://svenskadikter.com/Viktor_Rydberg
   - Swedish poetry archive

## How to Collect Poems

### Method 1: Manual Collection (for initial batch)

Since automated access to Archive.org is currently restricted, manual collection is recommended:

1. **Download the Anthology PDF**
   - Visit: https://upload.wikimedia.org/wikipedia/commons/6/64/Anthology_of_Swedish_lyrics_from_1750_to_1915;_(IA_cu31924026327076).pdf
   - Or borrow from Archive.org: https://archive.org/details/anthologyofswedi00stor
   - Find Rydberg's section (check table of contents)

2. **Get Swedish Originals from Runeberg**
   - Visit: https://runeberg.org/rydbdikt/
   - Each poem has its own page
   - Copy the Swedish text

3. **Create Paired Files**
   ```bash
   # Example for poem 1 (Tomten)
   echo "Swedish poem text here" > poems/rydberg/poem1-swedish.txt
   echo "English translation here" > poems/rydberg/poem1-english.txt
   ```

### Method 2: Use Python Collection Script

If available, use the manual poem collector:

```bash
cd /home/user/Trainingdata
python3 scripts/manual_poem_collector.py --author rydberg
```

### Method 3: Wikisource

Check for available poems on Wikisource:
- English: https://en.wikisource.org/wiki/Author:Viktor_Rydberg
- Swedish: https://sv.wikisource.org/wiki/Författare:Viktor_Rydberg

## Tips for Collection

1. **Start with "Tomten"** - It's the most famous and widely available with translations

2. **Use the JSONL template** - Refer to `/home/user/Trainingdata/data/rydberg_poems_template.jsonl` for the complete list

3. **Verify pairs** - Ensure each Swedish poem has a matching English translation
   ```bash
   ls poems/rydberg/*.txt | wc -l
   # Should be even number (pairs of Swedish/English)
   ```

4. **Check Swedish originals** - All Rydberg poems from the anthology should be on Runeberg.org

5. **Archive.org alternatives**:
   - Try different Archive.org mirrors
   - Some may allow downloading full text
   - PDF version can be downloaded and text extracted

## Collection Strategy

### Priority 1: Well-documented poems (Start here)
- Tomten (The House-Goblin) - Most famous, multiple translations available
- De badande barnen (The Bathing Children) - Mentioned in research
- Den nya Grottesången (The New Grotti Song) - Well-documented

### Priority 2: Poems with direct Runeberg links
- All poems listed above have Swedish originals on Runeberg
- English translations in Stork's anthology

### Priority 3: Additional poems
- Other Rydberg poems not in Stork's anthology
- May have different translators

## Copyright Status

All materials are **public domain**:
- Viktor Rydberg died in 1895 (all works in public domain worldwide)
- Charles Wharton Stork's 1917 translations (public domain in USA)
- Archive.org and Runeberg.org resources are freely available

## Progress Tracking

Check current collection status:
```bash
# Count collected poems
ls poems/rydberg/*-swedish.txt 2>/dev/null | wc -l

# List collected poems
ls -1 poems/rydberg/*.txt
```

## Goal

Collect all 22 poem pairs from Stork's anthology, with potential for additional Rydberg poems beyond the anthology.

## Additional Resources

- Viktor Rydberg biography: https://en.wikipedia.org/wiki/Viktor_Rydberg
- Britannica entry: https://www.britannica.com/biography/Viktor-Rydberg
- Complete works (14 volumes): https://runeberg.org/authors/rydberg.html
- "Tomten" poem analysis: https://en.wikipedia.org/wiki/Tomten_(poem)

## Questions?

See the main repository documentation for similar collection efforts:
- Fröding collection: `poems/froding/README.md`
- Collection templates: `data/*_poems_template.jsonl`
