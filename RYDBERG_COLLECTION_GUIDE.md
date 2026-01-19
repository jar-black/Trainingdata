# Viktor Rydberg Poem Collection Guide

## Quick Start

This guide helps you collect 22+ Viktor Rydberg poems with both Swedish originals and English translations.

## What Has Been Created

1. **Directory Structure**: `/home/user/Trainingdata/poems/rydberg/`
2. **Template File**: `/home/user/Trainingdata/data/rydberg_poems_template.jsonl` (22 poems identified)
3. **Collection Script**: `/home/user/Trainingdata/scripts/collect_rydberg_poems.py`
4. **README**: `/home/user/Trainingdata/poems/rydberg/README.md`

## Collection Sources

### English Translations (22 poems)

**Primary Source: Anthology of Swedish Lyrics from 1750 to 1915** (1917)
- Translator: Charles Wharton Stork
- Archive.org: https://archive.org/details/anthologyofswedi00stor
- PDF version: https://upload.wikimedia.org/wikipedia/commons/6/64/Anthology_of_Swedish_lyrics_from_1750_to_1915;_(IA_cu31924026327076).pdf
- Public domain (published 1917)

### Swedish Originals

**Primary Source: Projekt Runeberg - Dikter av Viktor Rydberg**
- Main collection: https://runeberg.org/rydbdikt/
- Individual poem URLs listed in template
- Public domain (Rydberg died 1895)

**Alternative Source: Swedish Wikisource**
- Author page: https://sv.wikisource.org/wiki/Författare:Viktor_Rydberg
- Individual poems available

## 22 Poems to Collect

All poems are listed in `/home/user/Trainingdata/data/rydberg_poems_template.jsonl`:

1. Tomten (The House-Goblin) - 1881
2. De badande barnen (The Bathing Children)
3. Den nya Grottesången (The New Grotti Song)
4. Dexippos (Dexippus) - 1876
5. Skogsrået (The Wood Nymph)
6. Snöfrid (Snowfrid)
7. Korpen (The Raven)
8. Drömliv (Dream Life)
9. På floden (On the River)
10. Kantat (Cantata)
11. En blomma (A Flower)
12. Höstkväll (Autumn Evening)
13. Den flygande holländaren (The Flying Dutchman)
14. Prometeus och Ahasverus (Prometheus and Ahasuerus)
15. Till ödet (To Fate)
16. Vaknen! (Awaken!)
17. Drömmaren (The Dreamer)
18. Vadan och varthän? (Whence and Whither?)
19. Älvan till flickan (The Elf to the Maiden)
20. Baldersbålet (Balder's Pyre)
21. Klockorna (The Bells)
22. Vinst och förlust (Gain and Loss)

## Collection Methods

### Method 1: Using the Collection Script (Recommended)

```bash
cd /home/user/Trainingdata
python3 scripts/collect_rydberg_poems.py
```

The script will:
1. Show your progress (poems collected vs remaining)
2. Prompt you with the next uncollected poem
3. Show you the source URLs for Swedish and English versions
4. Let you paste the poem text
5. Automatically save files as `poem1-swedish.txt`, `poem1-english.txt`, etc.
6. Update the JSONL database

### Method 2: Manual Collection

#### Step 1: Get the Anthology PDF

Download from Wikimedia Commons:
```
https://upload.wikimedia.org/wikipedia/commons/6/64/Anthology_of_Swedish_lyrics_from_1750_to_1915;_(IA_cu31924026327076).pdf
```

Or borrow from Archive.org (requires free account):
```
https://archive.org/details/anthologyofswedi00stor
```

#### Step 2: Find Rydberg's Section

1. Open the PDF
2. Check the Table of Contents
3. Find "Viktor Rydberg" section (should have 22 poems)
4. Note the page numbers

#### Step 3: Get Swedish Originals

Visit Projekt Runeberg:
```
https://runeberg.org/rydbdikt/
```

Click on individual poem titles to get full text.

#### Step 4: Create Paired Files

For each poem:

```bash
# Example for Tomten (poem #1)
cd /home/user/Trainingdata/poems/rydberg

# Create Swedish version
cat > poem1-swedish.txt << 'EOF'
[Paste Swedish text from Runeberg here]
EOF

# Create English version
cat > poem1-english.txt << 'EOF'
[Paste English translation from Stork anthology here]
EOF
```

### Method 3: Using Wikisource

Some poems are available on Swedish Wikisource:

1. **Tomten**: https://sv.wikisource.org/wiki/Tomten
2. Check author page for more: https://sv.wikisource.org/wiki/Författare:Viktor_Rydberg

## Specific Poem Resources

### "Tomten" (The House-Goblin) - Start Here!

This is Rydberg's most famous poem, published in 1881.

**Swedish text sources:**
- Wikisource: https://sv.wikisource.org/wiki/Tomten
- Runeberg: https://runeberg.org/rydbdikt/tomten.html
- Kalliope: https://kalliope.org/en/text/rydberg2001051001

**English translation sources:**
- Charles Wharton Stork (1930): http://plover.net/~agarvin/faerie/poems/House_Goblin.html
- Poetry Nook: https://www.poetrynook.com/poem/house-goblin
- LyricsTranslate (multiple versions): https://lyricstranslate.com/en/tomten-tomten.html
- Anthology of Swedish Lyrics (1917) - Archive.org

**Opening lines:**
- Swedish: "Midvinternattens köld är hård..."
- English (Stork): "Cold is the night, and still, and strange..."

### Other Well-Documented Poems

**Dexippos** (1876)
- Swedish: https://runeberg.org/rydbdikt/dexippos.html
- Swedish (vrsidor.se): http://vrsidor.se/Dikt/dexippos.html
- English: In Stork's anthology

**De badande barnen** (The Bathing Children)
- Mentioned as giving "intimate pictures of Swedish country life"
- Swedish: https://runeberg.org/rydbdikt/
- English: In Stork's anthology

## Collection Strategy

### Week 1: High-Priority Poems (Start here)

1. **Tomten** - Most famous, multiple sources
2. **Dexippos** - Well-documented
3. **De badande barnen** - Frequently mentioned
4. **Den nya Grottesången** - Historical significance (social commentary)

### Week 2: Mythological/Philosophical Poems

5. **Baldersbålet** (Balder's Pyre)
6. **Prometeus och Ahasverus** (Prometheus and Ahasuerus)
7. **Skogsrået** (The Wood Nymph)
8. **Snöfrid** (Snowfrid)
9. **Älvan till flickan** (The Elf to the Maiden)

### Week 3: Shorter Lyrics

10. **En blomma** (A Flower)
11. **Höstkväll** (Autumn Evening)
12. **På floden** (On the River)
13. **Drömliv** (Dream Life)
14. **Korpen** (The Raven)

### Week 4: Remaining Poems

15-22. Complete the collection with remaining poems

## Checking Your Progress

View collection statistics:
```bash
python3 scripts/collect_rydberg_poems.py --stats
```

Count collected poems:
```bash
ls poems/rydberg/*-swedish.txt | wc -l
```

Verify pairs (should be even number):
```bash
ls poems/rydberg/*.txt | wc -l
```

List all collected poems:
```bash
ls -1 poems/rydberg/*.txt
```

## Tips for Success

### 1. Start with Tomten

"Tomten" is the easiest to find with multiple available sources. Use it to:
- Test the collection workflow
- Verify the file format
- Ensure the script works correctly

### 2. Download the PDF First

Download the Anthology PDF to your computer:
- You can work offline
- Easier to copy/paste text
- No web access issues

### 3. Use Runeberg Systematically

Runeberg has all Swedish originals with consistent URLs:
```
https://runeberg.org/rydbdikt/[poemname].html
```

### 4. Match Poems Carefully

Ensure Swedish and English versions match:
- Check title correspondence
- Verify stanza count matches
- Compare first/last lines

### 5. Preserve Formatting

When pasting poems:
- Keep stanza breaks (blank lines)
- Preserve indentation
- Don't add extra whitespace at beginning/end

### 6. Track Progress

The script automatically tracks which poems are collected. Use `--stats` frequently to see progress.

## Common Issues and Solutions

### Issue: Can't access Archive.org

**Solution**: Use the Wikimedia Commons PDF link:
```
https://upload.wikimedia.org/wikipedia/commons/6/64/Anthology_of_Swedish_lyrics_from_1750_to_1915;_(IA_cu31924026327076).pdf
```

### Issue: Runeberg page not loading

**Solution**: Try Archive.org mirror:
```
https://archive.org/stream/arkivkopia.se-runeberg-rydbdikt/rydbdikt_djvu.txt
```

### Issue: Text has OCR errors

**Solution**:
- Compare multiple sources
- Check Wikisource versions (community-corrected)
- Cross-reference with other digitizations

### Issue: Can't find specific translation

**Solution**:
- Verify poem is in Stork's anthology (check table of contents)
- Some poems may have alternate translations
- Check LyricsTranslate for community translations

## File Format

Each poem creates two files:

**poemN-swedish.txt**:
```
Midvinternattens köld är hård,
stjärnorna gnistra och glimma.
Alla sova i enslig gård
djupt under midnattstimma.
...
```

**poemN-english.txt**:
```
Cold is the night, and still, and strange,
Stars they glitter and shimmer.
All are asleep in the lonely grange
Under the midnight's glimmer.
...
```

## Database Format

The JSONL database automatically tracks:
- Poem titles (Swedish and English)
- Collection and year
- Translator
- Source URLs
- Full text of both versions
- Poem number
- File paths
- Collection date

## Next Steps After Collection

Once you've collected poems, you can:

1. **Verify completeness**:
   ```bash
   python3 scripts/collect_rydberg_poems.py --stats
   ```

2. **Review quality**:
   - Check for OCR errors
   - Verify translations match originals
   - Ensure proper formatting

3. **Use for training**:
   - Machine translation models
   - Bilingual language models
   - Swedish-English alignment
   - Literary translation research

## Legal and Copyright

All materials are **public domain**:
- Viktor Rydberg died in 1895 (works entered public domain in 1946)
- Charles Wharton Stork's 1917 translations (public domain in USA)
- Translations published before 1928 are public domain in USA
- All sources (Archive.org, Runeberg, Wikisource) are legally accessible

## Questions or Issues?

See:
- Main README: `/home/user/Trainingdata/poems/rydberg/README.md`
- Template file: `/home/user/Trainingdata/data/rydberg_poems_template.jsonl`
- Similar project: `/home/user/Trainingdata/poems/froding/` (Gustaf Fröding collection)

## Goal

**Target**: 22 poem pairs (Swedish-English)

**Stretch goal**: Additional Rydberg poems beyond Stork's anthology

**Timeline**: Aim for 5-6 poems per week = complete in 4 weeks

Good luck with your collection!
