import librosa, numpy as np

def extract_features(y, sr, n_mfcc=13):
    feats = []
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
    feats.extend(np.mean(mfcc, axis=1))
    feats.extend(np.std(mfcc, axis=1))
    feats.append(np.mean(librosa.feature.spectral_centroid(y=y, sr=sr)))
    feats.append(np.mean(librosa.feature.spectral_bandwidth(y=y, sr=sr)))
    feats.append(np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr)))
    feats.append(np.mean(librosa.feature.zero_crossing_rate(y)))
    feats.append(np.mean(librosa.feature.rms(y=y)))
    return np.array(feats)
