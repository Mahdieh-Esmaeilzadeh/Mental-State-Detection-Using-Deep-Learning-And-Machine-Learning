import joblib

def save_model(model, path="experiments/models/model.pkl"):
    joblib.dump(model, path)

def load_model(path="experiments/models/model.pkl"):
    return joblib.load(path)
