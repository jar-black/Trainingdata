# Esaias Tegnér Poems Collection

This directory contains Esaias Tegnér's poems in paired Swedish-English format.

## About Esaias Tegnér

**Esaias Tegnér** (1782-1846) was a Swedish teacher, bishop, and the most popular poet of his period. He was a leading representative of Swedish Romanticism.

### Major Works:
- **Svea** (1811) - Patriotic poem that won Swedish Academy prize
- **Nattvardsbarn / The Children of the Lord's Supper** (1820) - Translated by Henry Wadsworth Longfellow (1841)
- **Frithiofs saga / Frithiof's Saga** (1825) - His greatest work, translated 22 times into English

## File Format

Each poem is stored as a pair of files:
- `poem1-swedish.txt` - Swedish original
- `poem1-english.txt` - English translation
- `poem2-swedish.txt` - Swedish original
- `poem2-english.txt` - English translation
- ...and so on

## Key Sources

### English Translations (Public Domain)

1. **"Poems by Tegnér"** - Archive.org
   - Contains "The Children of the Lord's Supper" (translated by Longfellow)
   - Contains "Frithiof's Saga" (translated by Rev. W. Lewery Blackley)
   - URL: https://archive.org/details/poemsbytegnrch00tegnuoft

2. **"Anthology of Swedish Lyrics from 1750 to 1915"** (1917)
   - 13 Tegnér poems translated by Charles Wharton Stork
   - URL: https://archive.org/details/anthologyofswedi00stor

3. **English Wikisource**
   - URL: https://en.wikisource.org/wiki/Author:Esaias_Tegnér

### Swedish Originals (Public Domain)

1. **Projekt Runeberg**
   - URL: http://runeberg.org/authors/tegner.html
   - Complete works available

2. **Swedish Wikisource**
   - URL: https://sv.wikisource.org/wiki/Författare:Esaias_Tegnér
   - Individual poems

## Known Poems with English Translations

1. **Svea** (1811) - Patriotic poem
2. **Nattvardsbarn / The Children of the Lord's Supper** (1820) - Trans: Longfellow
3. **Frithiofs saga / Frithiof's Saga** (1825) - Trans: Multiple (22 English translations exist)
4. **Axel** (1822) - Narrative poem
5. Plus 13 poems from Stork's Anthology (1917)

## How to Collect Poems

### Method 1: Use the Collection Script

```bash
cd /home/user/Trainingdata
python3 scripts/collect_tegner_poems.py
```

### Method 2: Manual Collection

1. Visit Archive.org sources above
2. Download or view the PDFs/texts
3. Create paired files manually:
   ```bash
   echo "Swedish text" > poems/tegner/poem1-swedish.txt
   echo "English text" > poems/tegner/poem1-english.txt
   ```

## Copyright Status

All materials are **public domain**:
- Esaias Tegnér died in 1846 (works entered public domain)
- Longfellow translations from 1841 (public domain)
- Stork translations from 1917 (public domain in USA)
- All other 19th century translations (public domain)

## Notable Translators

- **Henry Wadsworth Longfellow** (1807-1882) - "The Children of the Lord's Supper"
- **Rev. W. Lewery Blackley** - "Frithiof's Saga"
- **Charles Wharton Stork** (1881-1971) - 13 poems in Anthology (1917)

## Goal

Collect at least 15-20 poem pairs initially. The Anthology of Swedish Lyrics alone contains 13 poems.
