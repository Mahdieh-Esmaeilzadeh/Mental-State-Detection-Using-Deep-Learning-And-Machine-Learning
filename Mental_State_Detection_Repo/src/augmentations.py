import librosa, numpy as np

def pitch_shift(y, sr, n_steps=2):
    return librosa.effects.pitch_shift(y, sr, n_steps=n_steps)

def add_noise(y, noise_level=0.005):
    noise = noise_level * np.random.normal(size=y.shape[0])
    return y + noise

def time_stretch(y, rate=1.1):
    return librosa.effects.time_stretch(y, rate)

def shift(y, sr, shift_max=0.1):
    shift = int(np.random.uniform(-shift_max, shift_max) * sr)
    return np.roll(y, shift)
