import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load the trained model (make sure you have the model.pkl in the same directory)
model = joblib.load('ann.pkl')

# Function to make predictions
def predict_employee_status(CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Geography_Germany, Geography_Spain, Gender_Male):
    input_data = np.array([[CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Geography_Germany, Geography_Spain, Gender_Male]])
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit App layout and inputs
st.markdown("""
    <style>
        .big-font {
            font-size:50px !important;
            color: #4CAF50;
            font-weight: bold;
        }
        .emoji {
            font-size: 40px;
        }
        .positive-message {
            color: #28a745;
            font-size: 20px;
            font-weight: bold;
        }
        .negative-message {
            color: #dc3545;
            font-size: 20px;
            font-weight: bold;
        }
        .title {
            font-size: 30px;
            color: #4CAF50;
        }
        .input-label {
            font-size: 18px;
            color: #555555;
        }
        .input-box {
            margin: 10px 0;
            background-color: #f1f1f1;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# App title and description
st.markdown('<p class="big-font">Employee Attrition Prediction</p>', unsafe_allow_html=True)

st.image("images.png", width=600, caption="Employee Attrition Prediction")

st.write("""
Welcome to the Employee Attrition Prediction app! This app helps you predict if an employee is likely to stay or leave the company based on various features.
""")

# User input section with different widgets for each feature

# CreditScore (Slider) 
st.markdown('<p class="input-label">💳 Credit Score</p>', unsafe_allow_html=True)
CreditScore = st.slider('Select the employee\'s credit score:', min_value=300, max_value=850, value=650, step=10, help="Select the employee's credit score.")

# Age (Slider)
st.markdown('<p class="input-label">👶 Age</p>', unsafe_allow_html=True)
Age = st.slider('Select the employee\'s age:', min_value=18, max_value=100, value=30, step=1, help="Select the employee's age.")

# Tenure (Slider)
st.markdown('<p class="input-label">📅 Tenure (years)</p>', unsafe_allow_html=True)
Tenure = st.slider('Select how many years the employee has been at the company:', min_value=0, max_value=10, value=5, step=1, help="Select how many years the employee has been at the company.")

# Balance (Slider)
st.markdown('<p class="input-label">💰 Balance</p>', unsafe_allow_html=True)
Balance = st.slider('Select the employee\'s current account balance:', min_value=0, max_value=250000, value=50000, step=1000, help="Select the employee's current account balance.")

# NumOfProducts (Box type with selectbox)
st.markdown('<p class="input-label">📊 Number of Products</p>', unsafe_allow_html=True)
NumOfProducts = st.selectbox('Select how many products the employee holds with the company:', options=[1, 2, 3, 4], index=1, help="Select how many products the employee holds with the company.")

# HasCrCard (Box type with selectbox)
st.markdown('<p class="input-label">💳 Has Credit Card</p>', unsafe_allow_html=True)
HasCrCard = st.selectbox('Does the employee have a credit card with the company?', options=['Yes', 'No'], index=0, help="Select whether the employee has a credit card with the company.")

# IsActiveMember (Box type with selectbox)
st.markdown('<p class="input-label">🌟 Is Active Member</p>', unsafe_allow_html=True)
IsActiveMember = st.selectbox('Is the employee an active member?', options=['Yes', 'No'], index=0, help="Select whether the employee is an active member of the company.")

# EstimatedSalary (Slider)
st.markdown('<p class="input-label">💸 Estimated Salary</p>', unsafe_allow_html=True)
EstimatedSalary = st.slider('Select the employee\'s estimated annual salary:', min_value=10000, max_value=200000, value=50000, step=1000, help="Select the employee's estimated annual salary.")

# Geography (Box type with multiselect to select country)
st.markdown('<p class="input-label">🌍 Geography</p>', unsafe_allow_html=True)
Geography = st.multiselect(
    'Select the geography where the employee is located:',
    options=['Germany', 'Spain', 'France', 'Italy'],
    default=['Germany'],
    help="Select the geography where the employee is located. You can select multiple if needed."
)

# Gender (Box type with selectbox)
st.markdown('<p class="input-label">🚻 Gender: Male</p>', unsafe_allow_html=True)
Gender_Male = st.selectbox('Select the gender of the employee:', options=['Yes', 'No'], index=0, help="Select whether the employee is male.")

# Convert checkbox-based selections into numerical binary values
Geography_Germany = 1 if 'Germany' in Geography else 0
Geography_Spain = 1 if 'Spain' in Geography else 0
Gender_Male = 1 if Gender_Male == 'Yes' else 0
HasCrCard = 1 if HasCrCard == 'Yes' else 0
IsActiveMember = 1 if IsActiveMember == 'Yes' else 0

# Predict button
if st.button('🔮 Predict'):
    # Call the prediction function with user inputs
    result = predict_employee_status(
        CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Geography_Germany, Geography_Spain, Gender_Male
    )
    
    # Display the result
    if result == 1:
        st.markdown('<p class="negative-message">🚨 Prediction: <strong>Employee will leave the company!</strong> 🚨</p>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="positive-message">😊 Prediction: <strong>Employee will stay in the company!</strong> 😊</p>', unsafe_allow_html=True)
