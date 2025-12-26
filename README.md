# 📡 Telecom Customer Churn Prediction

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Framework](https://img.shields.io/badge/Framework-Streamlit-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

## 📜 Project Overview
This project aims to predict **Customer Churn** in the telecommunications industry using Machine Learning. By analyzing historical customer data (demographics, services, and account information), the system identifies customers who are likely to discontinue their service. This allows telecom providers to take proactive retention measures.

The project was developed as part of the **Applied AI** program at **Gopal Narayan Singh University**.

---

## 🚀 Live Demo
Check out the live deployment of the project here:
**[[Link to your Streamlit App](https://mangal1910-deploymodeltest-app-try4ws.streamlit.app/#telecom-customer-churn-prediction)]

---

## 📂 Dataset
The dataset used is the standard **Telco Customer Churn** dataset.
* **Source:** [Kaggle - Telco Customer Churn](https://www.kaggle.com/blastchar/telco-customer-churn)
* **Records:** 7,043 rows
* **Features:** 21 columns (including Target variable `Churn`)
* **Key Attributes:** `Tenure`, `MonthlyCharges`, `TotalCharges`, `Contract`, `PaymentMethod`, `InternetService`.

---

## 🛠️ Tech Stack
* **Programming Language:** Python
* **Libraries:**
    * `Pandas` (Data Manipulation)
    * `NumPy` (Numerical Operations)
    * `Scikit-Learn` (Machine Learning Algorithms)
    * `Matplotlib` / `Seaborn` (Data Visualization)
    * `Streamlit` (Web Application Framework)
* **Tools:** Jupyter Notebook, VS Code, Git/GitHub.

---

## ⚙️ Project Workflow
1.  **Data Preprocessing:**
    * Handled missing values in `TotalCharges`.
    * Removed non-predictive columns (`customerID`).
    * Encoded categorical variables using `OneHotEncoder`.
    * Scaled numerical features using `StandardScaler`.
2.  **Model Training:**
    * Tested algorithms: Logistic Regression, Decision Tree, Random Forest.
    * Selected the best performing model based on Accuracy and Recall.
3.  **Deployment:**
    * Built an interactive web interface using **Streamlit**.
    * Allowed users to input customer details and get real-time churn predictions.

---

## 🏃‍♂️ How to Run Locally

Follow these steps to run the project on your local machine:

### 1. Clone the Repository
```bash
git clone [https://github.com/mangal1910/DeployModeltest](https://github.com/your-username/telecom-churn-prediction.git)
cd telecom-churn-prediction