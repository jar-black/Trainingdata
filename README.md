# Trainingdata

Synthetic conversation datasets and notebooks for fine-tuning LLMs.

## Contents
- `data/age_prediction_dataset.jsonl`: 32 balanced age-labeled conversations formatted for instruction tuning.
- `data/age_prediction_dataset_sv.jsonl`: Swedish-language variant with the same structure and label coverage.
- `notebooks/unsloth_age_prediction_training.ipynb`: Jupyter workflow to train an age-range classifier on top of `unsloth/llama-3-3b-instruct` using a single RTX 3060 12GB GPU.

## Usage
1. Open the notebook in JupyterLab (or VS Code). 
2. Follow the installation cell to pull Unsloth and its dependencies.
3. Run the configuration cell to load the JSONL dataset (set `DATA_PATH` to the Swedish file if you want to fine-tune on the localized data).
4. Train the LoRA adapters with the provided hyperparameters tailored for 12GB VRAM.
5. Export the adapter weights from `checkpoints/age-predictor` for deployment or merging.
