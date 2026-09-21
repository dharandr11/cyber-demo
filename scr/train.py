import os
import sys
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.preprocess import load_data, prepare_data


DATA_PATH = "data/network_traffic.csv"
MODEL_PATH = "models/classifier.pkl"
ENCODER_PATH = "models/encoders.pkl"


print("Loading dataset...")

df = load_data(DATA_PATH)

print("Dataset shape:", df.shape)

X, y, encoders = prepare_data(df)

print("Features:", list(X.columns))

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("Training Random Forest...")

model = RandomForestClassifier(
    n_estimators=150,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)
recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)
f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)

print("\n========== MODEL RESULTS ==========")

print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    zero_division=0
))

# Save model
os.makedirs("models", exist_ok=True)

joblib.dump(model, MODEL_PATH)
joblib.dump(encoders, ENCODER_PATH)

print("\nModel saved to:", MODEL_PATH)
print("Encoders saved to:", ENCODER_PATH)