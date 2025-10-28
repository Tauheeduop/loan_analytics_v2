'''''
import streamlit as st
import pandas as pd
from modules.model_predictor import load_and_train

st.set_page_config(page_title="Loan Analytics v2", layout="wide")

st.title("🏦 Loan Approval Insight Dashboard (v2.0)")
#st.markdown("Automatic model training and prediction using local dataset.")

# Train model automatically
#st.info("🚀 Training model on local dataset `data/loan_train.csv`...")

model, acc, features, label_encoders = load_and_train()
#st.success(f"✅ Model trained successfully! Accuracy: {acc:.2f}")

#st.divider()
st.subheader("🔮 Predict Loan Approval")

# Define user input fields
user_input = {}
for feature in features:
    user_input[feature] = st.number_input(f"{feature}", value=0.0)

if st.button("Predict"):
    input_df = pd.DataFrame([user_input])
    pred = model.predict(input_df)[0]
    st.success(f"🎯 Prediction: {'Approved ✅' if pred == 1 else 'Rejected ❌'}")
'''''
import streamlit as st
import pandas as pd
from modules.model_predictor import load_and_train

st.set_page_config(page_title="Loan Approval Predictor", layout="wide")

st.title("🏦 Smart Loan Approval Assistant (Agentic Frontend)")

st.info("Model is being trained automatically from dataset...")
model, acc, features, label_encoders = load_and_train()
st.success(f"✅ Model ready! Accuracy: {acc:.2f}")

st.markdown("### 🧾 Enter Applicant Details")

# --- User Form ---
gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Term (in days)", min_value=0)
credit_history = st.selectbox("Credit History", [1.0, 0.0])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

# --- Prediction ---
if st.button("Predict Loan Approval"):
    # Prepare input
    input_dict = {
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_area
    }

    input_df = pd.DataFrame([input_dict])

    # Encode categorical features
    for col, le in label_encoders.items():
        if col in input_df.columns:
            input_df[col] = le.transform(input_df[col])

    # Predict
    prediction = model.predict(input_df)[0]
    st.success(f"🎯 Result: {'Approved ✅' if prediction == 1 else 'Rejected ❌'}")
