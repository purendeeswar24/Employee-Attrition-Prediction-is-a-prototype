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
st.title('Employee Attrition Prediction')

st.write("""
This app predicts whether an employee will stay or leave the company based on various features like credit score, age, tenure, salary, and more.
""")

# User input section
CreditScore = st.slider('Credit Score', min_value=300, max_value=850, value=650)
Age = st.slider('Age', min_value=18, max_value=100, value=30)
Tenure = st.slider('Tenure (years)', min_value=0, max_value=10, value=5)
Balance = st.slider('Balance', min_value=0, max_value=250000, value=50000)
NumOfProducts = st.slider('Number of Products', min_value=1, max_value=4, value=2)
HasCrCard = st.radio('Has Credit Card', options=[1, 0], index=0)
IsActiveMember = st.radio('Is Active Member', options=[1, 0], index=0)
EstimatedSalary = st.slider('Estimated Salary', min_value=10000, max_value=200000, value=50000)
Geography_Germany = st.radio('Geography: Germany', options=[1, 0], index=0)
Geography_Spain = st.radio('Geography: Spain', options=[1, 0], index=0)
Gender_Male = st.radio('Gender: Male', options=[1, 0], index=0)

# Predict button
if st.button('Predict'):
    # Call the prediction function with user inputs
    result = predict_employee_status(
        CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary, Geography_Germany, Geography_Spain, Gender_Male
    )
    
    # Display the result
    if result == 1:
        st.write("Prediction: **Employee will leave the company**")
    else:
        st.write("Prediction: **Employee will stay in the company**")
