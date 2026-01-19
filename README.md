# Trainingdata

Training datasets and notebooks for fine-tuning LLMs on Swedish poetry translation.

## Contents

### English to Swedish Poetry Translation
- `data/english_to_swedish_poetry_translation.json`: **790 translation examples** from **46 poems** in Alpaca format
- `notebooks/unsloth_translation_training.ipynb`: Complete Jupyter workflow to train a poetry translator using Unsloth with `llama-3.2-3b-instruct` on RTX 3060 12GB GPU
- `scripts/generate_training_data.py`: Automated script to generate training data from all poem files

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
1. **Generate training data** (optional - already done):
   - Run `python3 scripts/generate_training_data.py` to regenerate from all poems
   - Creates 790 examples from 46 complete poems
2. **Train the model**:
   - Open `notebooks/unsloth_translation_training.ipynb` in JupyterLab or VS Code
   - Install Unsloth and dependencies
   - The notebook includes automatic train/validation split (95%/5%)
   - Optimized for RTX 3060 12GB: 2 epochs, batch size 2, gradient accumulation 4
   - Training time: ~30-60 minutes depending on GPU
3. **Test and export**:
   - Test translations with provided examples
   - Save as LoRA adapters, merged 16-bit, or GGUF format

### Swedish Poetry Collections
The repository contains bilingual (Swedish-English) poem collections from major Swedish poets:
- **Viktor Rydberg** (1828-1895): "Tomten" and other philosophical works
- **Verner von Heidenstam** (1859-1940): Travel and national romantic poetry
- **Esaias Tegnér** (1782-1846): "Frithiofs saga" and other epic works
- **Gustaf Fröding** (1860-1911): Lyrical and folk-inspired poetry
- **Erik Axel Karlfeldt** (1864-1931): Nature and rural life poetry

These collections serve as the source material for the translation training data.
