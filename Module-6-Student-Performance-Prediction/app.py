
from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st


# --------------------------------------------------
# 1. Configure the application
# --------------------------------------------------

BASE_DIR = Path(__file__).parent
MODEL_FILE = BASE_DIR / "model.pkl"

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="centered",
)

st.title("🎓 Student Performance Prediction System")

st.write(
    "Estimate a student's final mathematics grade "
    "using a machine learning model."
)

st.caption(
    "Educational demonstration only. Predictions are estimates, "
    "not guaranteed grades or professional assessments."
)

st.divider()


# --------------------------------------------------
# 2. Load the trained model
# --------------------------------------------------

if not MODEL_FILE.exists():
    st.error(
        "The trained model was not found. "
        "Open the terminal and run: python train_model.py"
    )
    st.stop()

try:
    saved_data = joblib.load(MODEL_FILE)
    model = saved_data["model"]
    features = saved_data["features"]

except Exception:
    st.error(
        "The model could not be loaded. "
        "Run python train_model.py again."
    )
    st.stop()


# --------------------------------------------------
# 3. Collect student information
# --------------------------------------------------

st.subheader("Enter Student Information")

studytime = st.selectbox(
    "Weekly study time",
    options=[1, 2, 3, 4],
    format_func=lambda value: {
        1: "1 - Less than 2 hours",
        2: "2 - 2 to 5 hours",
        3: "3 - 5 to 10 hours",
        4: "4 - More than 10 hours",
    }[value],
)

failures = st.number_input(
    "Number of past class failures",
    min_value=0,
    max_value=4,
    value=0,
    step=1,
)

absences = st.number_input(
    "Number of school absences",
    min_value=0,
    max_value=100,
    value=2,
    step=1,
)

g1 = st.slider(
    "First-period grade (G1)",
    min_value=0,
    max_value=20,
    value=10,
)

g2 = st.slider(
    "Second-period grade (G2)",
    min_value=0,
    max_value=20,
    value=12,
)


# --------------------------------------------------
# 4. Generate a prediction
# --------------------------------------------------

if st.button("Predict Final Grade", type="primary"):

    input_data = pd.DataFrame(
        [[studytime, failures, absences, g1, g2]],
        columns=features,
    )

    prediction = float(model.predict(input_data)[0])

    # Keep the displayed grade within the dataset's 0-20 scale.
    prediction = max(0.0, min(20.0, prediction))

    st.divider()
    st.subheader("Prediction Result")

    st.metric(
        label="Estimated Final Grade (G3)",
        value=f"{prediction:.1f} / 20",
    )

    if prediction >= 10:
        st.success(
            "The estimated grade is at or above 10 out of 20."
        )
    else:
        st.warning(
            "The estimated grade is below 10 out of 20. "
            "Consider reviewing study habits and learning needs."
        )

    # Display previous grades and the estimated grade.
    chart_data = pd.DataFrame(
        {
            "Grade": ["G1", "G2", "Estimated G3"],
            "Score": [g1, g2, prediction],
        }
    )

    fig, ax = plt.subplots(figsize=(7, 4))

    ax.bar(chart_data["Grade"], chart_data["Score"])
    ax.set_ylim(0, 20)
    ax.set_ylabel("Grade out of 20")
    ax.set_title("Previous Grades and Estimated Final Grade")

    st.pyplot(fig)
    plt.close(fig)

    st.info(
        "This estimate uses study time, past failures, absences, "
        "and earlier grades. It may be inaccurate for individual "
        "students or students from other schools."
    )


# --------------------------------------------------
# 5. Show project information
# --------------------------------------------------

with st.expander("About this project"):
    st.write(
        "This application uses a Random Forest regression model "
        "trained on the UCI Student Performance dataset."
    )

    st.write("Input features:")
    st.write(", ".join(features))

    st.write("Target variable: G3 (final mathematics grade).")

    st.write(
        "The model estimates a numerical grade. It does not "
        "guarantee academic outcomes and should not be used "
        "for high-stakes decisions."
    )
