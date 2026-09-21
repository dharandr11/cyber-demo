import pandas as pd
from sklearn.preprocessing import LabelEncoder


def load_data(file_path):
    df = pd.read_csv(file_path)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove completely empty rows
    df = df.dropna(how="all")

    return df


def prepare_data(df, target_column="Attack"):

    # Remove rows where target is missing
    df = df.dropna(subset=[target_column])

    # Convert target to binary
    df[target_column] = (
        df[target_column]
        .astype(str)
        .str.upper()
        .map(lambda x: 0 if x == "NORMAL" else 1)
    )

    # Remove rows that could not be converted
    df = df.dropna(subset=[target_column])

    X = df.drop(columns=[target_column])
    y = df[target_column].astype(int)

    # Encode categorical columns
    categorical_columns = X.select_dtypes(
        include=["object"]
    ).columns

    encoders = {}

    for column in categorical_columns:
        encoder = LabelEncoder()

        X[column] = encoder.fit_transform(
            X[column].astype(str)
        )

        encoders[column] = encoder

    # Replace infinite values
    X = X.replace([float("inf"), float("-inf")], 0)

    # Fill missing numeric values
    X = X.fillna(0)

    return X, y, encoders