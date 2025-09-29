Mental State Detection from Speech

This repository contains a research and implementation project focused on detecting mental and emotional states from human speech using machine learning and deep learning techniques. The project is designed to explore how audio features can be leveraged to infer emotional and mental states, providing insights into affective computing and speech emotion recognition (SER).

Project Overview

Human speech conveys rich information beyond words—it carries emotions, stress, and mental cues. This project leverages these audio signals to identify mental states using advanced feature extraction, augmentation, and neural network modeling.

Key components include:

Feature Extraction: MFCCs, spectral features, pitch, zero-crossing rate (ZCR), and RMS energy are extracted from audio recordings.

Data Augmentation: Techniques such as pitch shifting, time stretching, noise addition, and shifting are applied to expand dataset diversity and improve model robustness.

Modeling:

Random Forest baseline models for quick experimentation.

Multi-Layer Perceptron (MLP) and CNN-GRU hybrid architectures for advanced deep learning.

Dual-channel spectrogram input (Mel + IMel) for richer frequency representation.

Evaluation: Performance is assessed using accuracy, F1-score, ROC curves, and confusion matrices. Hierarchical and pairwise classifications are also implemented.

Features

📊 Exploratory Analysis: Visualizations of feature distributions and PCA for dimensionality insights.

🎵 Audio Preprocessing: Automatic trimming, padding, and normalization of raw audio files.

🧪 Experimentation-Ready: Notebooks for feature extraction, data augmentation, and model training.

💾 Reproducibility: Seeded random operations and consistent preprocessing pipelines.

Dataset

The project is compatible with datasets organized as:

DATA_PATH/<label>/*.wav


where each folder represents a different emotional or mental state. Augmentation and spectrogram generation scripts allow easy scaling for larger datasets.

Potential Applications

Mental health monitoring

Human-computer interaction (HCI) and voice assistants

Emotion-aware AI in education, gaming, and healthcare

Speech-based affective research

Repository Structure (Suggested)
/data                   # Raw or processed audio files
/notebooks
    exploration.ipynb    # Feature analysis and EDA
    training.ipynb       # Model building, training, evaluation
/src
    features.py          # Feature extraction scripts
    augmentation.py      # Audio augmentation functions
    models.py            # CNN/GRU model definitions
/experiments
    models               # Saved model weights and encoders
README.md

Future Work

Incorporate multimodal data (e.g., text, video) for improved prediction accuracy.

Explore transfer learning and pre-trained audio embeddings.

Apply cross-corpus validation to enhance generalization.

Experiment with real-time mental state detection pipelines.
