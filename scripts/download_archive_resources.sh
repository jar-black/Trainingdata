#!/bin/bash
#
# Download Gustaf Fröding poem resources from Internet Archive
#
# These are public domain materials that can be freely downloaded.
# The script downloads both text and PDF versions of key resources.
#

set -e

# Create downloads directory
DOWNLOAD_DIR="downloads/archive_org"
mkdir -p "$DOWNLOAD_DIR"

echo "=========================================="
echo "Downloading Gustaf Fröding Resources"
echo "from Internet Archive"
echo "=========================================="
echo ""

# Function to download with progress
download_file() {
    local url="$1"
    local output="$2"
    echo "Downloading: $(basename "$output")"
    echo "From: $url"
    curl -L --progress-bar -o "$output" "$url" || {
        echo "Warning: Download failed for $url"
        return 1
    }
    echo "Saved to: $output"
    echo ""
}

# 1. Anthology of Swedish Lyrics (1917) - Text version
echo "[1/6] Anthology of Swedish Lyrics - Text Version"
download_file \
    "https://archive.org/stream/anthologyofswedi00stor/anthologyofswedi00stor_djvu.txt" \
    "$DOWNLOAD_DIR/anthology_swedish_lyrics_1917.txt"

# 2. Anthology of Swedish Lyrics - PDF version
echo "[2/6] Anthology of Swedish Lyrics - PDF Version"
download_file \
    "https://upload.wikimedia.org/wikipedia/commons/6/64/Anthology_of_Swedish_lyrics_from_1750_to_1915;_(IA_cu31924026327076).pdf" \
    "$DOWNLOAD_DIR/anthology_swedish_lyrics_1917.pdf"

# 3. Selected Poems (1916) - Text version
echo "[3/6] Selected Poems by Gustaf Fröding - Text Version"
download_file \
    "https://archive.org/stream/in.ernet.dli.2015.42774/2015.42774.Gustaf-Froding_djvu.txt" \
    "$DOWNLOAD_DIR/selected_poems_1916.txt"

# 4. Alternative anthology text
echo "[4/6] Anthology of Swedish Lyrics - Alternative Text"
download_file \
    "https://archive.org/stream/anthologyswedis00storgoog/anthologyswedis00storgoog_djvu.txt" \
    "$DOWNLOAD_DIR/anthology_swedish_lyrics_alt.txt"

# 5. Gustaf Fröding in America text
echo "[5/6] Gustaf Fröding in America"
download_file \
    "https://archive.org/stream/GustafFrodingInAmerica/02GustafFrdingPoems1916_djvu.txt" \
    "$DOWNLOAD_DIR/froding_in_america_1916.txt"

# 6. Gitarr och dragharmonika from Litteraturbanken
echo "[6/6] Gitarr och dragharmonika (Swedish original)"
download_file \
    "https://archive.org/download/arkivkopia.se-littbank-FrodingG_GuitarrOchDragharmonika1893/FrodingG_GuitarrOchDragharmonika1893.pdf" \
    "$DOWNLOAD_DIR/gitarr_och_dragharmonika_1893.pdf"

echo ""
echo "=========================================="
echo "Download Complete!"
echo "=========================================="
echo ""
echo "Files saved to: $DOWNLOAD_DIR"
echo ""
echo "Next steps:"
echo "1. Review the downloaded files"
echo "2. Extract poem texts from the resources"
echo "3. Match Swedish originals with English translations"
echo "4. Populate data/froding_poems_template.jsonl with the texts"
echo ""
echo "Key Resources:"
echo "- Anthology of Swedish Lyrics: 37 Fröding poems in English"
echo "- Selected Poems: English translations by Stork (1916)"
echo "- Gitarr och dragharmonika: Swedish originals (1891)"
echo ""
