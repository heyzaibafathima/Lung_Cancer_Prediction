
import streamlit as st
import pandas as pd
import pickle

st.set_page_config(
    page_title="Cancer Prediction",
    page_icon="🩺",
    layout="centered"
)

# Brown and beige theme
st.markdown("""
<style>
.stApp {
    background-color: #F5EFE6;
    color: #49372C;
}
h1, h2, h3, p, label {
    color: #49372C !important;
}
div.stButton > button {
    background-color: #795548;
    color: white;
    border-radius: 8px;
    border: none;
    height: 45px;
    font-size: 17px;
    font-weight: bold;
}
div.stButton > button:hover {
    background-color: #5D4037;
    color: white;
}
div[data-testid="stForm"] {
    background-color: #EDE0D0;
    padding: 20px;
    border-radius: 12px;
    border: 1px solid #D4BDA8;
}
</style>
""", unsafe_allow_html=True)

# Load trained model
with open("cancer_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Cancer Prediction")
st.write("Enter the patient's details to predict the diagnosis.")
st.divider()

with st.form("prediction_form"):

    st.subheader("Patient Details")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input(
            "Age", min_value=20, max_value=80, value=45
        )

        gender = st.selectbox(
            "Gender", ["Male", "Female"]
        )

        bmi = st.number_input(
            "BMI", min_value=15.0, max_value=40.0,
            value=25.5, step=0.1
        )

        smoking = st.selectbox(
            "Smoking", ["No", "Yes"]
        )

    with col2:
        genetic_risk = st.selectbox(
            "Genetic Risk", [0, 1, 2],
            format_func=lambda x: {
                0: "Low (0)",
                1: "Medium (1)",
                2: "High (2)"
            }[x]
        )

        physical_activity = st.number_input(
            "Physical Activity", min_value=0, value=5
        )

        alcohol_intake = st.number_input(
            "Alcohol Intake", min_value=0, value=2
        )

        cancer_history = st.selectbox(
            "Cancer History", ["No", "Yes"]
        )

    predict = st.form_submit_button(
        "Predict", use_container_width=True
    )

if predict:

    # Encode categorical inputs
    gender_value = 0 if gender == "Male" else 1
    smoking_value = 0 if smoking == "No" else 1
    history_value = 0 if cancer_history == "No" else 1

    # Prepare the eight input features
    patient = pd.DataFrame([{
        "Age": age,
        "Gender": gender_value,
        "BMI": bmi,
        "Smoking": smoking_value,
        "GeneticRisk": genetic_risk,
        "PhysicalActivity": physical_activity,
        "AlcoholIntake": alcohol_intake,
        "CancerHistory": history_value
    }])

    # Predict using the trained model
    prediction = model.predict(patient)[0]

    st.divider()
    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("Prediction: Cancer")
    else:
        st.success("Prediction: No Cancer")

    st.caption(
        "Educational project only. This model's output is not "
        "a medical diagnosis."
    )
