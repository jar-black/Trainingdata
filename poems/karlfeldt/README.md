# Erik Axel Karlfeldt Poem Collection

## About Erik Axel Karlfeldt (1864-1931)

Erik Axel Karlfeldt was a Swedish poet whose highly symbolist poetry masquerading as regionalism was immensely popular. He won the 1931 Nobel Prize in Literature posthumously. He had been offered the award already in 1919 but refused to accept it because of his position as permanent secretary to the Swedish Academy (1913-1931).

His poetry is characterized by themes of nature, love, and life in the province of Dalarna, combining regionalism with French symbolist influences.

## Poetry Collections (in chronological order)

1. **Vildmarks- och kärleksvisor** (1895) - "Songs of Wilderness and of Love"
2. **Fridolins visor** (1898) - "Fridolin's Songs"
3. **Fridolins lustgård** (1901) - "Fridolin's Pleasure Garden"
   - Includes "Dalmålningar på rim" (Dalecarlian Frescoes in Rhyme)
4. **Flora och Pomona** (1906) - "Flora and Pomona"
5. **Flora och Bellona** (1918) - "Flora and Bellona"
6. **Hösthorn** (1927) - "The Horn of Autumn"

## Public Domain Status

- **Swedish Originals**: All public domain (Karlfeldt died 1931)
- **English Translations**: Charles Wharton Stork translations from 1917 are public domain; 1938 translations may be subject to different copyright depending on jurisdiction

## Primary English Translation Sources

### 1. Anthology of Swedish Lyrics from 1750 to 1915 (1917)
- **Translator**: Charles Wharton Stork
- **Archive.org**: https://archive.org/details/anthologyofswedi00stor
- **Content**: Contains 27 Karlfeldt poems with English translations
- **Status**: Public domain
- **Access**: Available on Archive.org (requires account or may need manual download)

### 2. Arcadia Borealis: Selected Poems (1938)
- **Translator**: Charles Wharton Stork
- **Publisher**: University of Minnesota Press
- **Illustrator**: Hilma Berglund (watercolors)
- **Archive.org**: https://archive.org/details/arcadiaborealiss0000char
- **Content**: Selected poems from all six volumes (1895-1927) plus posthumous collection (1934)
- **Pages**: viii, 145 pages
- **Organization**: Grouped by mood rather than chronology
- **Special Note**: Contains a "disproportionately large number" of Dalecarlian Frescoes
- **Status**: First edition limited to 500 copies; copyright status varies by jurisdiction

### 3. Poetry Magazine (June 1932)
- **Title**: "Erik Axel Karlfeldt, Swedish Poet"
- **Author**: Charles Wharton Stork
- **URL**: https://www.poetryfoundation.org/poetrymagazine/browse?contentId=59553
- **Content**: Article about Karlfeldt with some translated poems

## Primary Swedish Original Sources

### Projekt Runeberg
- **Main Author Page**: https://runeberg.org/authors/karlfeldt.html
- **Fridolins visor**: https://runeberg.org/fridvisa/
- **Status**: Public domain, digitized Swedish texts
- **Format**: HTML with full text of poems

### Additional Resources
- **Babel Web Anthology**: https://www.babelmatrix.org/works/sv-en/Karlfeldt,_Erik_Axel-1864/works
  - Bilingual resources with Swedish originals and English translations

## Collection Strategy

### Target: 25-30 Poem Pairs

The template file `/home/user/Trainingdata/data/karlfeldt_poems_template.jsonl` contains metadata for 30 poems, selected based on:
1. Poems known to appear in both the 1917 Anthology and 1938 Arcadia Borealis
2. Representative poems from each of Karlfeldt's six major collections
3. Famous poems including "Dalecarlian Frescoes," "Fridolin's Pleasure Garden," and others

## Manual Collection Instructions

Due to access restrictions on Archive.org and other sources, poems need to be collected manually:

### Step 1: Access Archive.org Sources

1. Create a free Archive.org account if needed
2. Access the 1917 Anthology: https://archive.org/details/anthologyofswedi00stor
3. Access the 1938 Arcadia Borealis: https://archive.org/details/arcadiaborealiss0000char
4. Download or view the full texts

### Step 2: Access Swedish Originals

1. Visit Projekt Runeberg: https://runeberg.org/authors/karlfeldt.html
2. Navigate to individual collections (e.g., Fridolins visor)
3. Copy Swedish text for each poem

### Step 3: Create Poem Files

For each poem in the template, create two files:
- `poem##-swedish.txt` - Swedish original
- `poem##-english.txt` - English translation by Stork

**Naming convention**:
- `poem01-swedish.txt` / `poem01-english.txt` - Vildmarkens sång / Song of the Wilderness
- `poem02-swedish.txt` / `poem02-english.txt` - Dröm och liv / Dream and Life
- etc.

**File format**:
```
Title: [Poem Title]
Author: Erik Axel Karlfeldt
Collection: [Collection Name]
Year: [Year]
Translator: [For English files only]

[Poem text with original line breaks]
```

### Step 4: Update JSONL Template

Once you have collected the actual poem texts, update the `karlfeldt_poems_template.jsonl` file:
- Replace `[To be filled]` placeholders with actual poem texts
- Verify metadata (title, year, collection)
- Add specific source URLs where texts were found

## Known Poem Titles to Prioritize

Based on references found in various sources, prioritize collecting these poems:

### From Arcadia Borealis (1938):
- Dalecarlian Frescoes in Rhyme (series of poems)
- Flower Song
- Harvest Moon
- Old-Fashioned Christmas
- Threnody
- Castle Unrest
- Sub Luna
- Fridolin's Pleasure Garden
- The Witch
- Dream and Life
- The Rhyme-Smith

### From Anthology of Swedish Lyrics (1917):
- All 27 Karlfeldt poems (check table of contents)

## Verification Checklist

For each collected poem:
- [ ] Swedish original text is complete
- [ ] English translation is complete
- [ ] Title matches in both languages
- [ ] Collection name is verified
- [ ] Publication year is correct
- [ ] Translator is credited (Charles Wharton Stork for most)
- [ ] Line breaks and stanza formatting preserved
- [ ] Special characters (å, ä, ö) correctly preserved in Swedish

## Additional Notes

### Translation Quality
Charles Wharton Stork was a respected translator of Scandinavian poetry and his translations are considered authoritative. He maintained close contact with Swedish literary circles and his work was praised for capturing the spirit of the originals.

### Dalecarlian Frescoes
This series of poems describing traditional wall paintings is particularly well-represented in Arcadia Borealis. These are narrative poems about Biblical scenes as depicted in Dalarna farmhouse art.

### Modern Availability
While the original books are in archives, some poems may be available on:
- Allmogens.se (Swedish folk culture site)
- LiederNet (song text database)
- Various poetry anthologies and academic works

## File Structure

```
/home/user/Trainingdata/
├── data/
│   └── karlfeldt_poems_template.jsonl   (metadata template - 30 poems)
└── poems/
    └── karlfeldt/
        ├── README.md                      (this file)
        ├── poem01-swedish.txt            (to be created)
        ├── poem01-english.txt            (to be created)
        ├── poem02-swedish.txt            (to be created)
        ├── poem02-english.txt            (to be created)
        └── ...                           (up to 30 pairs)
```

## Copyright Notice

All Swedish original texts are in the public domain (author died 1931). English translations by Charles Wharton Stork from 1917 are in the public domain in the United States. The 1938 Arcadia Borealis translations may have different copyright status depending on jurisdiction and when Stork died. Verify copyright status for your specific use case.

## Sources and References

- NobelPrize.org: https://www.nobelprize.org/prizes/literature/1931/karlfeldt/
- Britannica: https://www.britannica.com/biography/Erik-Axel-Karlfeldt
- Wikipedia: https://en.wikipedia.org/wiki/Erik_Axel_Karlfeldt
- Projekt Runeberg: https://runeberg.org/authors/karlfeldt.html
- Archive.org Anthology: https://archive.org/details/anthologyofswedi00stor
- Archive.org Arcadia Borealis: https://archive.org/details/arcadiaborealiss0000char
