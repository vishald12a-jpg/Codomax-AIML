
from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import train_test_split


# --------------------------------------------------
# 1. Load the dataset
# --------------------------------------------------

DATA_FILE = Path(__file__).parent / "student-mat.csv"

if not DATA_FILE.exists():
    raise FileNotFoundError(
        "student-mat.csv was not found. "
        "Download the UCI dataset and place it beside train_model.py."
    )

df = pd.read_csv(DATA_FILE, sep=";")

print("=" * 50)
print("STUDENT PERFORMANCE PREDICTION")
print("=" * 50)

print("\nDataset loaded successfully!")
print("Dataset shape:", df.shape)

print("\nFirst five rows:")
print(df.head())


# --------------------------------------------------
# 2. Select input features and target
# --------------------------------------------------

features = ["studytime", "failures", "absences", "G1", "G2"]
target = "G3"

missing_columns = [
    column for column in features + [target]
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Required columns are missing: {missing_columns}"
    )

X = df[features]
y = df[target]

print("\nInput features:", features)
print("Target variable:", target)


# --------------------------------------------------
# 3. Split data into training and testing sets
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))


# --------------------------------------------------
# 4. Create and train the regression model
# --------------------------------------------------

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
)

model.fit(X_train, y_train)

print("\nModel training completed successfully!")


# --------------------------------------------------
# 5. Predict grades for the test data
# --------------------------------------------------

y_pred = model.predict(X_test)


# --------------------------------------------------
# 6. Evaluate model performance
# --------------------------------------------------

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nMODEL EVALUATION")
print("-" * 40)
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R-squared Score (R2): {r2:.3f}")


# --------------------------------------------------
# 7. Save the model and its feature names
# --------------------------------------------------

MODEL_FILE = Path(__file__).parent / "model.pkl"

joblib.dump(
    {
        "model": model,
        "features": features,
        "target": target,
    },
    MODEL_FILE,
)

print("\nTrained model saved successfully!")
print("Model location:", MODEL_FILE)
print("\nYou can now run: streamlit run app.py")
print("=" * 50)
