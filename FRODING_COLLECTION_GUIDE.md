# Gustaf Fröding Poems Collection Guide

This guide provides comprehensive information for collecting Gustaf Fröding poems with both Swedish originals and English translations.

## Identified Poem Pairs (16 poems with both versions available)

### From Gitarr och dragharmonika (1891)
1. **Gitarr och dragharmonika / Guitar and Concertina**
2. **En hög visa / A Song-Of-Songs**
3. **Vackert väder / Lovely Weather**
4. **Indianer / Indians**
5. **Vallarelåt / Pastoral**
6. **Skogsrån / The Wood Sprite**
7. **Våran prost / Our Dean**
8. **Äktenskapsfrågan / Matrimonial Queries**
9. **Det var dans bort i vägen / The Ball**

### From Nya dikter (1894)
10. **Idealism och realism / Idealism and Realism**
11. **Den gamla goda tiden / The Good Old Days**

### From Stänk och flikar (1896)
12. **I ungdomen / In Youth**
13. **Strövtåg i hembygden / A Stroll Through the Local Countryside**

### From Gralstänk (1898)
14. **Friheten / Freedom**

### Collection Unknown
15. **En kärleksvisa / A Ditty About Love**
16. **Säv, säv, susa / Rush, Rush, Whisper**

## Primary Sources

### Swedish Originals

1. **Project Runeberg** (Public Domain)
   - Gitarr och dragharmonika: https://runeberg.org/dragharm/
   - Stänk och flikar: https://runeberg.org/stanflik/
   - Individual poems have direct links (e.g., /dragharm/aktfraga.html)

2. **Litteraturbanken** (Swedish Literature Bank)
   - Digital editions with EPUB/PDF downloads
   - Archive.org mirrors: https://archive.org/details/arkivkopia.se-littbank-FrodingG_GuitarrOchDragharmonika1893

3. **Svenska Dikter**
   - https://svenskadikter.com/Gustaf_Fröding
   - Individual poem pages

4. **Svensk-poesi.com**
   - Individual poems with Swedish text

### English Translations

1. **Charles Wharton Stork - "Selected Poems" (1916)**
   - Internet Archive: https://archive.org/details/selectedpoems00frodiala
   - Alternative link: https://archive.org/details/in.ernet.dli.2015.42774
   - Full text (if accessible): https://archive.org/stream/in.ernet.dli.2015.42774/2015.42774.Gustaf-Froding_djvu.txt

2. **Charles Wharton Stork - "Anthology of Swedish Lyrics from 1750 to 1915" (1917)**
   - Contains 37 Fröding poems (most represented poet)
   - Internet Archive: https://archive.org/details/anthologyofswedi00stor
   - Alternative: https://archive.org/details/anthologyswedis00storgoog
   - PDF download: https://upload.wikimedia.org/wikipedia/commons/6/64/Anthology_of_Swedish_lyrics_from_1750_to_1915;_(IA_cu31924026327076).pdf
   - Full text: https://archive.org/stream/anthologyofswedi00stor/anthologyofswedi00stor_djvu.txt

3. **Allmogens.se** (Modern translations)
   - Idealism och realism: https://allmogens.se/en/poetry/idealism-och-realism/
   - I ungdomen: https://allmogens.se/en/poetry/i-ungdomen/
   - Friheten: https://allmogens.se/en/poetry/friheten/
   - Den gamla goda tiden: https://allmogens.se/en/poetry/den-gamla-goda-tiden/
   - Strövtåg i hembygden: https://allmogens.se/en/poetry/strovtag-i-hembygden/

4. **LyricsTranslate.com**
   - En kärleksvisa: https://lyricstranslate.com/en/en-k%C3%A4rleksvisa-ditty-about-love.html
   - Vackert väder: https://lyricstranslate.com/en/vackert-vader-lovely-weather.html
   - Säv, säv, susa: https://lyricstranslate.com/en/sav-sav-susa-rush-rush-whisper.html-0

5. **Project Gutenberg**
   - Modern Swedish Masterpieces (short stories, not poems): https://www.gutenberg.org/files/64808/64808-h/64808-h.htm
   - Gustaf Fröding biography by Ida Bäckmann: https://www.gutenberg.org/ebooks/75504

## Collection Strategy

### Option 1: Manual Collection from Websites
1. Visit each Swedish source and copy poem text
2. Visit corresponding English source and copy translation
3. Paste into the JSONL template file

### Option 2: Download Archive.org Resources
1. Download the "Anthology of Swedish Lyrics" PDF or text file
2. Download the "Selected Poems" from Archive.org
3. Access Swedish originals from Project Runeberg or Litteraturbanken
4. Extract and match poems manually

### Option 3: Use Web Scraping (if allowed)
- Create a Python script using requests/beautifulsoup4
- Respect robots.txt and terms of service
- Add delays between requests

## Data Format

The template file `data/froding_poems_template.jsonl` uses this structure:

```json
{
  "swedish_title": "Poem title in Swedish",
  "english_title": "Poem title in English",
  "swedish_text": "Full Swedish poem text",
  "english_text": "Full English translation",
  "collection": "Original collection name",
  "year": 1891,
  "translator": "Translator name",
  "source_swedish": "URL to Swedish source",
  "source_english": "URL to English source"
}
```

## Copyright and Public Domain Status

- **Gustaf Fröding's works**: Public domain (author died 1911)
- **Charles Wharton Stork translations (1916-1917)**: Public domain in the USA
- **Modern translations**: Check individual copyright status
- **Allmogens.se translations**: Verify license/copyright
- **LyricsTranslate.com**: Check contributor licenses

## Additional Poem Candidates

The "Anthology of Swedish Lyrics" contains 37 Fröding poems. Beyond the 16 identified above, you can find more by:
1. Downloading the anthology and checking the table of contents
2. Comparing with Swedish sources to find matching poems
3. Potentially collecting 20-30+ poem pairs total

## Next Steps

1. Download the Archive.org resources (PDF/text files)
2. Access the websites listed above to view individual poems
3. Populate the template JSONL file with actual poem texts
4. Verify all poems have both Swedish and English versions
5. Format consistently for training data use

## References

- [Gustaf Fröding - Wikipedia](https://en.wikipedia.org/wiki/Gustaf_Fr%C3%B6ding)
- [Project Runeberg - Gustaf Fröding](https://runeberg.org/authors/froding.html)
- [Wikisource - Gustaf Fröding](https://en.wikisource.org/wiki/Author:Gustaf_Fröding)
- [Internet Archive - Selected Poems](https://archive.org/details/selectedpoems00frodiala)
- [Internet Archive - Anthology of Swedish Lyrics](https://archive.org/details/anthologyofswedi00stor)
