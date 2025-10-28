# modules/model_predictor.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def load_and_train():
    # --- Load dataset ---
    df = pd.read_csv("data/loan_train.csv")

    # --- Basic cleaning ---
    df = df.drop_duplicates()
    df = df.fillna(df.mode().iloc[0])

    # Encode categorical variables
    label_encoders = {}
    for col in df.select_dtypes(include=["object"]).columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    # --- Split data ---
    X = df.drop("Loan_Status", axis=1)
    y = df["Loan_Status"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # --- Train model ---
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # --- Accuracy ---
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)

    return model, acc, X.columns, label_encoders
