# Mental State Detection from Speech

This project focuses on **detecting mental states from human speech** using
Machine Learning (ML) and Deep Learning (DL) approaches.

---

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

---

## Repository Structure
data/ → raw & processed datasets (e.g., IEMOCAP, SAVEE, EMODB)
notebooks/ → Colab/Jupyter notebooks for training & experiments
src/ → core source code (data loading, features, models, training, evaluation)
experiments/ → logs, trained models, visualizations, reports
docs/ → project proposal, literature review, thesis documentation

yaml
Copy code

---

## Installation / Usage
Install required packages:

```bash
pip install -r requirements.txt
You can then run notebooks in notebooks/ to train and evaluate models.

Dataset
The dataset used in this project is not publicly available due to privacy and research restrictions.

Researchers who wish to access the dataset may request it by contacting: [rezvanizahra@gmail.com].

Please note that the dataset can only be shared for non-commercial, educational, and research purposes.

Ownership
This project is a student research project conducted at Alzahra University.
All intellectual property rights and the original credit of this project belong to Alzahra University.

License
Use of this code and dataset is allowed only for non-commercial, educational, and research purposes.
Any use must credit the authors and Alzahra University, and clearly indicate any modifications.
Commercial use or redistribution for profit is prohibited.

The project is provided "as is" without any warranties. Users are responsible for any consequences arising from its use.

markdown
Copy code

---