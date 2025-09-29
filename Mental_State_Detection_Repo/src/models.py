from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

def get_random_forest():
    return RandomForestClassifier(n_estimators=200, random_state=42)

def get_mlp():
    return MLPClassifier(hidden_layer_sizes=(128,64), max_iter=500, random_state=42)
