# Manual Collection Guide for Tegnér Poems

Due to network access restrictions, this guide provides step-by-step instructions for manually collecting Esaias Tegnér's poems with Swedish originals and English translations.

## Target: 13-15 Poem Pairs

### Priority Poems to Collect

#### From Stork's "Anthology of Swedish Lyrics" (1917) - 13 Poems

**Source**: https://archive.org/details/anthologyofswedi00stor

1. **Flyttfåglarna / Birds of Passage** (poem1)
2. **Jätten / The Giant** (poem2)
3. **Det eviga / The Eternal** (poem3)
4. **Kyssar / Kisses** (poem4)
5. **Sång till solen / Song to the Sun** (poem5)
6. **Additional 8 poems from Stork anthology** (poem6-13)

#### From Other Sources

7. **Nattvardsbarn / The Children of the Lord's Supper** (poem14)
   - Swedish: Projekt Runeberg http://runeberg.org/tepoems/
   - English: Longfellow translation
   - Note: This is a long narrative poem (~1000 lines)

8. **Frithiofs saga / Frithiof's Saga** (poem15+)
   - 24 cantos - can be collected as individual poems
   - Swedish: Projekt Runeberg or Swedish Wikisource
   - English: Multiple translations available
     - Rev. W. Lewery Blackley (recommended)
     - Project Gutenberg: https://www.gutenberg.org/ebooks/59689
     - Longfellow translated excerpts: "Frithiof's Homestead", "Frithiof's Temptation", "Frithiof's Farewell"

## Collection Process

### Step 1: Access Archive.org (Stork Anthology)

1. Visit: https://archive.org/details/anthologyofswedi00stor
2. Click "Read Online" or "Download"
3. Find Tegnér section (pages 36-50 approximately)
4. For each poem:
   - Copy English translation
   - Note the Swedish title given
   - Save to `poemN-english.txt`

### Step 2: Collect Swedish Originals

#### Option A: Swedish Wikisource
1. Visit: https://sv.wikisource.org/wiki/Författare:Esaias_Tegnér
2. Find each poem by Swedish title
3. Copy full text
4. Save to `poemN-swedish.txt`

#### Option B: Projekt Runeberg
1. Visit: http://runeberg.org/authors/tegner.html
2. Navigate to "Samlade skrifter" (Collected Works)
3. Find each poem
4. Copy text
5. Save to `poemN-swedish.txt`

### Step 3: Collect from Project Gutenberg

For Frithiof's Saga cantos:
1. Visit: https://www.gutenberg.org/ebooks/59689
2. Download plain text or HTML version
3. Extract individual cantos
4. Save each canto as `poem15-english.txt`, `poem16-english.txt`, etc.

For Swedish versions:
1. Visit: https://www.gutenberg.org/ebooks/8518
2. Download Swedish version
3. Extract corresponding cantos

### Step 4: Longfellow Translations

For Longfellow's translations of Frithiof excerpts:
1. Visit: https://en.wikisource.org/wiki/Author:Esaias_Tegnér
2. Or: https://allpoetry.com (search for Longfellow + Tegnér)
3. Collect:
   - Frithiof's Homestead
   - Frithiof's Temptation
   - Frithiof's Farewell
   - A Sledge-ride on the Ice

## File Naming Convention

- Swedish originals: `poemN-swedish.txt`
- English translations: `poemN-english.txt`
- Where N = 1, 2, 3, ...

## Updating Metadata

After collecting each poem, update `/home/user/Trainingdata/data/tegner_poems.jsonl`:

```json
{
  "poem_id": "poem1",
  "swedish_title": "Flyttfåglarna",
  "english_title": "Birds of Passage",
  "swedish_text": "[full text here]",
  "english_text": "[full text here]",
  "translator": "Charles Wharton Stork",
  "year": null,
  "source_swedish": "https://sv.wikisource.org/wiki/Flyttfåglarna_(Tegnér)",
  "source_english": "Anthology of Swedish Lyrics (1917), Archive.org",
  "author": "Esaias Tegnér",
  "author_years": "1782-1846",
  "language_pair": "sv-en"
}
```

## Alternative Accessible Sources

If Archive.org is blocked:

1. **Google Books**: Search for "Anthology of Swedish Lyrics Stork"
   - Preview may show full pages

2. **EbooksRead.com**: https://www.ebooksread.com/authors-eng/charles-wharton-stork/anthology-of-swedish-lyrics-from-1750-to-1915-rot/

3. **HathiTrust**: https://catalog.hathitrust.org/ (search for Tegnér)

4. **Local Libraries**: Many university libraries have digitized versions

## Quick Start Commands

Run these after collecting poems manually:

```bash
# Count collected poems
ls -1 poems/tegner/*-swedish.txt | wc -l
ls -1 poems/tegner/*-english.txt | wc -l

# Verify pairs
for f in poems/tegner/*-swedish.txt; do
    base=$(basename "$f" -swedish.txt)
    if [ ! -f "poems/tegner/${base}-english.txt" ]; then
        echo "Missing English: $base"
    fi
done

# Update JSONL with collected texts
python3 scripts/update_tegner_jsonl.py
```

## Notes on Copyright

All sources are public domain:
- Tegnér died in 1846 (works in public domain worldwide)
- Stork translations from 1917 (public domain in USA)
- Longfellow translations from 1841 (public domain)
- Other 19th century translations (public domain)

## Contact for Help

If you need assistance accessing these sources, consider:
- Using a VPN if sources are geo-blocked
- Contacting your library for interlibrary loan
- Checking if local Swedish cultural centers have collections
