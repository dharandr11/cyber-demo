import joblib
import pandas as pd


MODEL_PATH = "models/classifier.pkl"
ENCODER_PATH = "models/encoders.pkl"


def load_model():

    model = joblib.load(MODEL_PATH)
    encoders = joblib.load(ENCODER_PATH)

    return model, encoders


def prepare_input(df, encoders):

    df = df.copy()

    for column, encoder in encoders.items():

        if column in df.columns:

            values = df[column].astype(str)

            known_values = set(encoder.classes_)

            df[column] = values.apply(
                lambda x: x if x in known_values else encoder.classes_[0]
            )

            df[column] = encoder.transform(
                df[column]
            )

    df = df.replace(
        [float("inf"), float("-inf")],
        0
    )

    df = df.fillna(0)

    return df


def predict_attack(df):

    model, encoders = load_model()

    X = prepare_input(df, encoders)

    predictions = model.predict(X)

    probabilities = model.predict_proba(X)

    attack_probability = probabilities[:, 1]

    return predictions, attack_probability