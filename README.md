# Trainingdata

Training datasets and notebooks for fine-tuning LLMs on Swedish poetry translation.

## Contents

### English to Swedish Poetry Translation
- `data/english_to_swedish_poetry_translation.json`: 25 translation examples in Alpaca format for English-to-Swedish poetry translation
- `notebooks/unsloth_translation_training.ipynb`: Complete Jupyter workflow to train a poetry translator using Unsloth with `llama-3.2-3b-instruct` on RTX 3060 12GB GPU

### Swedish Poets Poetry Collections
- `data/froding_poems_template.jsonl`: Gustaf Fröding poem pairs (Swedish-English)
- `data/tegner_poems.jsonl`: Esaias Tegnér poem pairs
- `data/rydberg_poems.jsonl`: Viktor Rydberg poem pairs
- `data/heidenstam_poems_template.jsonl`: Verner von Heidenstam poem pairs
- `data/karlfeldt_poems_template.jsonl`: Erik Axel Karlfeldt poem pairs
- `poems/`: Original Swedish and English text files for 600+ poems
- `scripts/collect_froding_poems.py`: Python utility to manage and export poem collection
- `scripts/scrape_froding_poems.py`: Web scraper for automated poem collection
- `scripts/download_archive_resources.sh`: Download public domain resources from Archive.org
- `FRODING_COLLECTION_GUIDE.md`: Comprehensive guide with sources and collection strategies
- `FRODING_SUMMARY.md`: Research summary and project overview

## Usage

### English to Swedish Translation Training
1. Open `notebooks/unsloth_translation_training.ipynb` in JupyterLab or VS Code
2. Install Unsloth and dependencies using the first cell
3. Configure training parameters (epochs, batch size, learning rate)
4. Load the training data from `data/english_to_swedish_poetry_translation.json`
5. Train the model using LoRA adapters optimized for 12GB VRAM
6. Test translations with the provided examples
7. Save model as LoRA adapters, merged 16-bit, or GGUF format

### Swedish Poetry Collections
The repository contains bilingual (Swedish-English) poem collections from major Swedish poets:
- **Viktor Rydberg** (1828-1895): "Tomten" and other philosophical works
- **Verner von Heidenstam** (1859-1940): Travel and national romantic poetry
- **Esaias Tegnér** (1782-1846): "Frithiofs saga" and other epic works
- **Gustaf Fröding** (1860-1911): Lyrical and folk-inspired poetry
- **Erik Axel Karlfeldt** (1864-1931): Nature and rural life poetry

These collections serve as the source material for the translation training data.
