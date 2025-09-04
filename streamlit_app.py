import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline
model = joblib.load("telco_churn_pipeline.joblib")

st.title("📊 Telecom Customer Churn Prediction")
st.write("Enter customer details to predict churn probability.")

# ----- User Inputs -----
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])
tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, step=1)
phone = st.selectbox("Phone Service", ["Yes", "No"])
multiple = st.selectbox("Multiple Lines", ["Yes", "No"])
internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_sec = st.selectbox("Online Security", ["Yes", "No"])
online_back = st.selectbox("Online Backup", ["Yes", "No"])
device_prot = st.selectbox("Device Protection", ["Yes", "No"])
tech_supp = st.selectbox("Tech Support", ["Yes", "No"])
stream_tv = st.selectbox("Streaming TV", ["Yes", "No"])
stream_mov = st.selectbox("Streaming Movies", ["Yes", "No"])
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless = st.selectbox("Paperless Billing", ["Yes", "No"])
payment = st.selectbox("Payment Method", ["Electronic check", "Mailed check", 
                                          "Bank transfer (automatic)", "Credit card (automatic)"])
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, step=1.0)
total_charges = st.number_input("Total Charges", min_value=0.0, step=1.0)

# ----- Create DataFrame -----
input_df = pd.DataFrame({
    "gender": [gender],
    "SeniorCitizen": [senior],
    "Partner": [partner],
    "Dependents": [dependents],
    "tenure": [tenure],
    "PhoneService": [phone],
    "MultipleLines": [multiple],
    "InternetService": [internet],
    "OnlineSecurity": [online_sec],
    "OnlineBackup": [online_back],
    "DeviceProtection": [device_prot],
    "TechSupport": [tech_supp],
    "StreamingTV": [stream_tv],
    "StreamingMovies": [stream_mov],
    "Contract": [contract],
    "PaperlessBilling": [paperless],
    "PaymentMethod": [payment],
    "MonthlyCharges": [monthly_charges],
    "TotalCharges": [total_charges]
})

# ----- Feature Engineering (same as training) -----
input_df["tenure_bin"] = pd.cut(
    input_df["tenure"],
    bins=[0, 12, 24, 48, 72],
    labels=["0-1yr", "1-2yr", "2-4yr", "4-6yr"]
)

input_df["charge_bin"] = pd.cut(
    input_df["MonthlyCharges"],
    bins=[0, 30, 60, 90, 120, 200],
    labels=["Low", "Medium", "High", "Very High", "Extreme"]
)

# ----- Prediction -----
if st.button("Predict Churn"):
    prob = model.predict_proba(input_df)[0][1]
    st.write(f"🔮 Churn Probability: **{prob:.2f}**")
    if prob > 0.5:
        st.error("⚠️ High chance of churn!")
    else:
        st.success("✅ Customer likely to stay.")
