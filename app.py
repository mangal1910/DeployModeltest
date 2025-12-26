import streamlit as st
import pandas as pd
import pickle
import numpy as np

# ==========================================
# 1. LOAD THE TRAINED MODEL
# ==========================================
try:
    model = pickle.load(open('model.pkl', 'rb'))
except FileNotFoundError:
    st.error("Error: 'model.pkl' file not found. Please upload it to the same directory.")
    st.stop()

# ==========================================
# 2. APP TITLE AND DESCRIPTION
# ==========================================
st.title("Telecom Customer Churn Prediction")
st.markdown("Enter customer details below to predict if they will churn (leave) or stay.")

# ==========================================
# 3. CREATE INPUT FIELDS (19 Features)
# ==========================================

# --- Section 1: Demographics ---
st.header("1. Demographic Information")
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"]) # Mapped to 0/1 later
    partner = st.selectbox("Partner", ["Yes", "No"])

with col2:
    dependents = st.selectbox("Dependents", ["Yes", "No"])

# --- Section 2: Account Information ---
st.header("2. Account Information")
col3, col4 = st.columns(2)

with col3:
    tenure = st.slider("Tenure (Months)", min_value=0, max_value=72, value=12)
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])

with col4:
    payment_method = st.selectbox("Payment Method", [
        "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
    ])
    monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, value=50.0)
    total_charges = st.number_input("Total Charges ($)", min_value=0.0, value=500.0)

# --- Section 3: Services ---
st.header("3. Services Signed Up")

col5, col6, col7 = st.columns(3)

with col5:
    phone_service = st.selectbox("Phone Service", ["Yes", "No"])
    multiple_lines = st.selectbox("Multiple Lines", ["No phone service", "No", "Yes"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

with col6:
    online_security = st.selectbox("Online Security", ["No internet service", "No", "Yes"])
    online_backup = st.selectbox("Online Backup", ["No internet service", "No", "Yes"])
    device_protection = st.selectbox("Device Protection", ["No internet service", "No", "Yes"])

with col7:
    tech_support = st.selectbox("Tech Support", ["No internet service", "No", "Yes"])
    streaming_tv = st.selectbox("Streaming TV", ["No internet service", "No", "Yes"])
    streaming_movies = st.selectbox("Streaming Movies", ["No internet service", "No", "Yes"])

# ==========================================
# 4. PREPARE DATA FOR PREDICTION
# ==========================================
if st.button("Predict Churn Status"):
    
    # Convert 'Senior Citizen' from Yes/No to 1/0
    senior_citizen_val = 1 if senior_citizen == "Yes" else 0

    # Create a DataFrame with the EXACT column names used in training
    # NOTE: The keys (left side) must match X_train.columns exactly.
    data = {
        'gender': [gender],
        'SeniorCitizen': [senior_citizen_val],
        'Partner': [partner],
        'Dependents': [dependents],
        'tenure': [tenure],
        'PhoneService': [phone_service],
        'MultipleLines': [multiple_lines],
        'InternetService': [internet_service],
        'OnlineSecurity': [online_security],
        'OnlineBackup': [online_backup],
        'DeviceProtection': [device_protection],
        'TechSupport': [tech_support],
        'StreamingTV': [streaming_tv],
        'StreamingMovies': [streaming_movies],
        'Contract': [contract],
        'PaperlessBilling': [paperless_billing],
        'PaymentMethod': [payment_method],
        'MonthlyCharges': [monthly_charges],
        'TotalCharges': [total_charges]
    }
    
    input_df = pd.DataFrame(data)

    # Display the input data (Optional - for debugging)
    # st.write(input_df)

    # ==========================================
    # 5. MAKE PREDICTION
    # ==========================================
    try:
        prediction = model.predict(input_df)
        
        # Check if the model supports probability prediction (optional)
        if hasattr(model, "predict_proba"):
            proba = model.predict_proba(input_df)[0][1] # Probability of Churn
            confidence = f"{proba * 100:.2f}%"
        else:
            confidence = "N/A"

        st.subheader("Prediction Result:")
        
        if prediction[0] == 1 or prediction[0] == 'Yes':
            st.error(f"⚠️ This Customer is Likely to CHURN (Leave).")
            if confidence != "N/A":
                st.write(f"Confidence Level: {confidence}")
        else:
            st.success(f"✅ This Customer is Likely to STAY.")
            if confidence != "N/A":
                st.write(f"Confidence Level: {100 - (float(confidence[:-1])):.2f}%")
                
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        st.info("Tip: Check if the column names in 'app.py' match exactly with your training dataset.")