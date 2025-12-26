import streamlit as st
import pandas as pd
import pickle

# 1. Load the model
filename = 'model.pkl' 
model = pickle.load(open(filename, 'rb'))

st.title("Telecom Customer Churn Prediction")

# 2. Create Inputs for ALL columns used in training
# (Group them nicely so it looks good)

st.header("Demographic Info")
gender = st.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["Yes", "No"])

st.header("Service Info")
tenure = st.number_input("Tenure (Months)", min_value=0, max_value=72, value=12)
phone_service = st.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["No internet service", "No", "Yes"])
# ... Add inputs for OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies ...

st.header("Contract & Billing")
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, value=50.0)
total_charges = st.number_input("Total Charges ($)", min_value=0.0, value=500.0)

# 3. Create the Predict Button
if st.button("Predict"):
    # CRITICAL STEP: Create a DataFrame with the EXACT column names as X_train
    # The keys (left side) MUST match X_train.columns exactly
    input_data = pd.DataFrame({
        'gender': [gender],
        'SeniorCitizen': [senior_citizen],
        'Partner': [partner],
        'Dependents': [dependents],
        'tenure': [tenure],
        'PhoneService': [phone_service],
        'MultipleLines': [multiple_lines],
        'InternetService': [internet_service],
        'OnlineSecurity': [online_security],
        # ... Include ALL other columns here ...
        'Contract': [contract],
        'PaperlessBilling': [paperless_billing],
        'PaymentMethod': [payment_method],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges]
    })

    # Make the prediction
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer is likely to CHURN.")
    else:
        st.success("Customer is likely to STAY.")