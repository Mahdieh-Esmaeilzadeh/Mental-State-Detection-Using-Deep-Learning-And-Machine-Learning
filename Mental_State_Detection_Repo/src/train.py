import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from src.features import extract_features
from src.data_loader import load_dataset
from src.models import get_random_forest, get_mlp

DATA_PATH = "data/processed"

X_raw, y = load_dataset(DATA_PATH)
X = [extract_features(x, 16000) for x in X_raw]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = get_random_forest()
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))
