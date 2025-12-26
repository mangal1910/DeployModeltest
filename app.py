import streamlit as st
import pickle
import numpy as np

# Load the model
model = pickle.load(open('model.pkl', 'rb'))

st.title("Telecom Customer Churn Prediction")

# Create inputs for the user
tenure = st.number_input("Tenure (Months)", min_value=0, max_value=72)
monthly_charges = st.number_input("Monthly Charges ($)")
total_charges = st.number_input("Total Charges ($)")

# Add other inputs (Contract, InternetService) as needed...

if st.button("Predict Churn"):
    # Prepare data for prediction (make sure it matches your model's expected input)
    input_data = [[tenure, monthly_charges, total_charges]] 
    prediction = model.predict(input_data)
    
    if prediction[0] == 1:
        st.error("Prediction: This Customer will CHURN (Leave).")
    else:
        st.success("Prediction: This Customer will STAY.")