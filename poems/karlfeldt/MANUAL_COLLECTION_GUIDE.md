# Manual Collection Guide for Karlfeldt Poems

## Network Access Limitations Encountered

During automated collection attempts, the following network restrictions were encountered:
- **WebFetch**: 403 Forbidden errors on all sources
- **wget**: Exit code 4 (network failure)
- **curl**: CONNECT tunnel failed, response 403
- **Python urllib**: Tunnel connection failed: 403 Forbidden

These restrictions prevent automated downloading from:
- Archive.org
- Projekt Runeberg (runeberg.org)
- Wikisource
- Allmogens.se
- BabelMatrix
- Poetry Foundation
- Google Books

## Verified Accessible Sources

Despite access restrictions in this environment, the following sources have been verified to exist and contain Karlfeldt poems:

### Swedish Originals

1. **Swedish Wikisource** (sv.wikisource.org)
   - Main collection: https://sv.wikisource.org/wiki/Erik_Axel_Karlfeldts_dikter
   - Category page: https://sv.wikisource.org/wiki/Kategori:Erik_Axel_Karlfeldt
   - Contains full Swedish texts of poems
   - Example poem "I älgtiden": https://sv.wikisource.org/wiki/I_%C3%A4lgtiden

2. **Projekt Runeberg**
   - Main author page: https://runeberg.org/authors/karlfeldt.html
   - Fridolins visor: https://runeberg.org/fridvisa/
   - Erik Axel Karlfeldts dikter: https://runeberg.org/eakdikt/

3. **Archive.org - Swedish Text Streams**
   - Hösthorn full text: https://archive.org/stream/arkivkopia.se-littbank-KarlfeldtEA_Hosthorn/KarlfeldtEA_Hosthorn_djvu.txt
   - Fridolins visor: https://archive.org/details/fridolinsvisoroc00karl

### English Translations

1. **Archive.org - 1917 Anthology of Swedish Lyrics**
   - Main page: https://archive.org/details/anthologyofswedi00stor
   - Full text stream: https://archive.org/stream/anthologyofswedi00stor/anthologyofswedi00stor_djvu.txt
   - Alternative: https://archive.org/stream/anthologyswedis00storgoog/anthologyswedis00storgoog_djvu.txt
   - Contains 27 Karlfeldt poems translated by Charles Wharton Stork

2. **Archive.org - 1938 Arcadia Borealis**
   - Main page: https://archive.org/details/arcadiaborealiss0000char
   - Selected poems from all six collections (1895-1927) plus posthumous (1934)

3. **Poetry Foundation**
   - Article with poems: https://www.poetryfoundation.org/poetrymagazine/articles/59553/erik-axel-karlfeldt-swedish-poet
   - "The Wooden Castle" poem: https://www.poetryfoundation.org/poetrymagazine/browse?contentId=19671
   - June 1932 issue: https://www.poetryfoundation.org/poetrymagazine/issue/70554/june-1932

4. **Allmogens.se - Bilingual Poems**
   - In the time of the moose: https://allmogens.se/en/poetry/i-algtiden/
   - The dream and life: https://allmogens.se/en/poetry/drommen-och-livet/
   - Sub luna: https://allmogens.se/en/poetry/sub-luna/
   - Lucia: https://allmogens.se/en/poetry/lucia/
   - Five dangerous F's: https://allmogens.se/en/poetry/fem-farliga-f/
   - Winter Rest: https://allmogens.se/en/poetry/vintervila/
   - The Fathers: https://allmogens.se/en/poetry/faderna/
   - Longing is my inheritance: https://allmogens.se/en/poetry/langtan-heter-min-arvedel/

5. **BabelMatrix**
   - Swedish-English works: https://www.babelmatrix.org/works/sv-en/Karlfeldt,_Erik_Axel-1864/works
   - "My forefathers" (Fäderna): https://www.babelmatrix.org/works/sv/Karlfeldt,_Erik_Axel-1864/F%C3%A4derna/en/38773-My_forefathers

## Manual Collection Steps

### Step 1: Access Swedish Originals from Wikisource

1. Go to https://sv.wikisource.org/wiki/Kategori:Erik_Axel_Karlfeldt
2. Look through the 209 available pages of Karlfeldt content
3. For each poem in the template (data/karlfeldt_poems_template.jsonl):
   - Search for the Swedish title on Wikisource
   - Copy the complete poem text
   - Save to `poems/karlfeldt/poemXX-swedish.txt`

### Step 2: Download Archive.org Books

#### Option A: Online Reader
1. Go to https://archive.org/details/anthologyofswedi00stor
2. Click "Read Online" or "Full Text"
3. Search for "KARLFELDT" to find his section
4. Copy each poem's English translation

#### Option B: Download Full Text
1. Go to the Archive.org item page
2. Click "DOWNLOAD OPTIONS" on the right sidebar
3. Select "Plain Text" or "DjVu Text"
4. Download the .txt file
5. Open in text editor and search for Karlfeldt poems

### Step 3: Extract Poems from Downloaded Texts

Use the Python script helper functions:
```python
from scripts.collect_karlfeldt_poems import parse_archive_org_text, create_poem_pair, load_template

# Load template
poems = load_template()

# For each poem, extract from downloaded text
with open('anthology1917.txt', 'r') as f:
    anthology_text = f.read()

# Extract individual poems
for i, poem in enumerate(poems, 1):
    english_text = parse_archive_org_text(anthology_text, poem['english_title'])
    if english_text:
        # Save English text
        ...
```

### Step 4: Match Swedish and English Pairs

For each of the 30 poems in the template:

1. Locate the Swedish original (from Wikisource or Runeberg)
2. Locate the English translation (from Archive.org books)
3. Verify they match using title and content clues
4. Create both files:
   - `poemXX-swedish.txt`
   - `poemXX-english.txt`

### Step 5: Validate and Update JSONL

After creating each pair:
```bash
cd /home/user/Trainingdata
python3 scripts/collect_karlfeldt_poems.py
```

This will validate files and show progress.

## Priority Collection Order

Based on verified availability, collect in this order:

### Tier 1: Available on Allmogens.se (8 poems with bilingual text)
These can be collected directly from allmogens.se which has both Swedish and English:

- I älgtiden / In the time of the moose
- Dröm och liv / The dream and life
- Sub luna / Sub Luna
- Lucia / Lucia
- Fem farliga F / Five dangerous F's
- Vintervila / Winter Rest
- Fäderna / The Fathers
- Längtan heter min arvedel / Longing is my inheritance

### Tier 2: In Template and Known to be in 1917 Anthology (from README)
These are confirmed to be in the 1917 Anthology:

- Fridolin's Song (Fridolins visa)
- Nocturne
- The Charcoal Burner's Daughter (Kolarflickan)
- The Wood-Nymph (Skogsrået)
- The Autumn Orchis (Höstorkan)
- The Market (Marknaden)
- A Winter Evening (En vinterafton)
- The Hunter Boy (Jägargossen)
- Love Song (Kärleksvisa)
- In a Dalecarlian Village (I en by i Dalarna)
- The Virgin Mary (Jungfru Maria)
- The Farmers' Guild (Böndernas gille)
- Autumn Hymn (Höstpsalm)

### Tier 3: In 1938 Arcadia Borealis
- Song of the Wilderness (Vildmarkens sång)
- Dream and Life (Dröm och liv)
- Fridolin's Pleasure Garden (Fridolins lustgård)
- Dalecarlian Frescoes in Rhyme (Dalmålningar på rim)
- The Witch (Häxan)
- Flower Song (Blomstervisa)
- Harvest Moon (Skördeman)
- My Forefathers (Min fäders jord)
- Old-Fashioned Christmas (Gammaldags jul)
- From the Crayfish Catcher's Song (Ur kräftfångarsången)
- Castle Unrest (Slottet Oro)
- Threnody (Likpredikan)
- Autumn Song (Höstlig visa)
- The Horn of Autumn (Hösthorn)
- The Milky Way (Vintergatan)

### Special Note: The Rhyme-Smith

Poem #15 "Rimsmeden" / "The Rhyme-Smith" is mentioned as being in Poetry Magazine (1932).
- May be available at: https://www.poetryfoundation.org/poetrymagazine/browse?contentId=59553
- Swedish original at: https://runeberg.org/fridvisa/2_1_01.html

## File Format Template

When creating poem files, use this exact format:

### Swedish File (poemXX-swedish.txt)
```
Title: [Swedish Title]
Author: Erik Axel Karlfeldt
Collection: [Collection Name]
Year: [Year]

[Poem text with original line breaks and stanza spacing]
```

### English File (poemXX-english.txt)
```
Title: [English Title]
Author: Erik Axel Karlfeldt
Collection: [Collection Name]
Year: [Year]
Translator: Charles Wharton Stork

[Poem text with original line breaks and stanza spacing]
```

## Verification Checklist

For each collected poem pair:
- [ ] Swedish title matches template
- [ ] English title matches template
- [ ] Both files have all required headers
- [ ] Poem text is complete (not truncated)
- [ ] Line breaks and stanzas preserved
- [ ] Swedish special characters (å, ä, ö) correct
- [ ] No OCR errors (for scanned sources)
- [ ] Files validated with script
- [ ] JSONL template updated with actual text

## Common Issues and Solutions

### OCR Errors in Archive.org Texts
- Compare multiple versions if available
- Cross-reference with Wikisource or other sources
- Common OCR mistakes: l↔I, rn↔m, c↔e

### Finding Exact Poem Matches
- Use title keywords to search in downloaded texts
- Look for collection names (Fridolins visor, Flora och Pomona, etc.)
- Check page numbers in README sources

### Missing Poems
- Some poems in template may not be in accessible sources
- Document which poems cannot be found
- Prioritize poems available in multiple sources

## Alternative Access Methods

If direct web access is restricted:

1. **Library Access**: Many university libraries have physical copies of Arcadia Borealis
2. **Interlibrary Loan**: Request scans through ILL services
3. **HathiTrust**: May have digitized versions with access
4. **Physical Books**: Search used book sites (AbeBooks, etc.)
5. **Academic Databases**: JSTOR, Project MUSE may have articles with full poems

## Progress Tracking

Use the helper script to check progress:

```bash
cd /home/user/Trainingdata
python3 -c "from scripts.collect_karlfeldt_poems import print_report; print_report()"
```

This will show:
- Number of poems with Swedish text
- Number of poems with English text
- Number of complete pairs
- Number of poem files created
- Overall completion percentage

## Contact and Resources

- **Karlfeldtsamfundet** (Karlfeldt Society): https://www.karlfeldt.org/
- **Swedish Literature Bank**: https://litteraturbanken.se/
- **Projekt Runeberg**: https://runeberg.org/
- **Swedish Wikisource**: https://sv.wikisource.org/

## Notes on Copyright

- **Swedish Originals**: Public domain (Karlfeldt died 1931)
- **1917 Translations**: Public domain in US (published pre-1928)
- **1938 Translations**: Copyright status varies by jurisdiction
- Charles Wharton Stork (1881-1971): Works may still be under copyright in some jurisdictions

For this training data project, we are using public domain sources only. The 1917 Anthology is clearly public domain. The 1938 Arcadia Borealis copyright status should be verified for your specific use case.
