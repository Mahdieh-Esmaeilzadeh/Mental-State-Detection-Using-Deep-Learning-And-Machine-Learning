import os
import librosa
import numpy as np

def load_audio(file_path, sr=16000):
    """Load and normalize audio file."""
    y, sr = librosa.load(file_path, sr=sr)
    y = librosa.util.normalize(y)
    return y, sr

def load_dataset(data_path, sr=16000):
    """Load dataset organized as data_path/<label>/<files>.wav"""
    X, y = [], []
    for label in os.listdir(data_path):
        label_dir = os.path.join(data_path, label)
        if not os.path.isdir(label_dir):
            continue
        for f in os.listdir(label_dir):
            if f.endswith(".wav"):
                try:
                    y_audio, _ = load_audio(os.path.join(label_dir, f), sr=sr)
                    X.append(y_audio)
                    y.append(label)
                except Exception:
                    continue
    return X, y
