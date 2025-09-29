# Mental State Detection from Speech

This project focuses on **detecting mental and emotional states from human speech** using
Machine Learning (ML) and Deep Learning (DL) approaches.

## Features
- 🎙️ **Speech Emotion Recognition (SER):** Detecting emotions from audio signals.
- 🧪 **Feature Extraction:** MFCCs, spectral features, zero-crossing rate, RMS, pitch.
- 🔄 **Data Augmentation:** Pitch shifting, noise injection, time-stretching, shifting.
- 🤖 **Models Implemented:** 
  - Random Forest (baseline)
  - Multi-layer Perceptron (MLP)
  - Deep learning models (CNN, RNN, GRU, Dual-channel CNN-SSAE, Bimodal fusion)
- 📊 **Evaluation Metrics:** Confusion matrix, ROC curve, accuracy, F1-score.
- 📚 **Documentation:** Literature review, thesis chapters, experiment reports.

## Repo Structure
- `data/` → raw & processed datasets (e.g., IEMOCAP, SAVEE, EMODB).
- `notebooks/` → Colab/Jupyter notebooks for training & experiments.
- `src/` → core source code (data loading, features, models, training, evaluation).
- `experiments/` → logs, trained models, visualizations, reports.
- `docs/` → project proposal, literature review, thesis documentation.

## Usage
```bash
pip install -r requirements.txt
