# Trainingdata

Synthetic conversation datasets and notebooks for fine-tuning LLMs.

## Contents

### Age Prediction Datasets
- `data/age_prediction_dataset.jsonl`: 32 balanced age-labeled conversations formatted for instruction tuning.
- `data/age_prediction_dataset_sv.jsonl`: Swedish-language variant with the same structure and label coverage.
- `notebooks/unsloth_age_prediction_training.ipynb`: Jupyter workflow to train an age-range classifier on top of `unsloth/llama-3-3b-instruct` using a single RTX 3060 12GB GPU.

### Gustaf Fröding Poetry Collection (In Progress)
- `data/froding_poems_template.jsonl`: Template for 16 identified poem pairs (Swedish-English translations)
- `scripts/collect_froding_poems.py`: Python utility to manage and export poem collection
- `scripts/scrape_froding_poems.py`: Web scraper for automated poem collection
- `scripts/download_archive_resources.sh`: Download public domain resources from Archive.org
- `FRODING_COLLECTION_GUIDE.md`: Comprehensive guide with sources and collection strategies
- `FRODING_SUMMARY.md`: Research summary and project overview

## Usage

### Age Prediction Training
1. Open the notebook in JupyterLab (or VS Code).
2. Follow the installation cell to pull Unsloth and its dependencies.
3. Run the configuration cell to load the JSONL dataset (set `DATA_PATH` to the Swedish file if you want to fine-tune on the localized data).
4. Train the LoRA adapters with the provided hyperparameters tailored for 12GB VRAM.
5. Export the adapter weights from `checkpoints/age-predictor` for deployment or merging.

### Gustaf Fröding Poems Collection
1. Review `FRODING_COLLECTION_GUIDE.md` for detailed source information
2. Download resources: `./scripts/download_archive_resources.sh`
3. Populate `data/froding_poems_template.jsonl` with actual poem texts
4. Check progress: `python3 scripts/collect_froding_poems.py --stats`
5. Export to training format: `python3 scripts/collect_froding_poems.py --export-training data/froding_training.jsonl`

**Status**: 16 poem pairs identified, ready for manual collection from public domain sources.
