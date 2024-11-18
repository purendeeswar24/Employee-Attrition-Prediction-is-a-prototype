# Employee Attrition Prediction using Deep Learning

## Project Overview

This project uses Artificial Neural Networks (ANN) to predict whether an employee will stay or leave the company. The model is trained on various factors such as employee demographics, account details, and company-related attributes. The goal is to build a predictive model that helps organizations identify employees who are likely to leave, allowing for targeted retention strategies.

### Features Used for Prediction:
- **CreditScore**: The credit score of the employee.
- **Age**: The age of the employee.
- **Tenure**: The number of years the employee has been with the company.
- **Balance**: The balance in the employee's account.
- **NumOfProducts**: The number of products the employee has with the company.
- **HasCrCard**: Whether the employee has a credit card (1 if yes, 0 if no).
- **IsActiveMember**: Whether the employee is an active member (1 if yes, 0 if no).
- **EstimatedSalary**: The employee's estimated annual salary.
- **Geography_Germany**: Whether the employee is based in Germany (1 if yes, 0 if no).
- **Geography_Spain**: Whether the employee is based in Spain (1 if yes, 0 if no).
- **Gender_Male**: Whether the employee is male (1 if male, 0 if female).

### Target Column:
- **Exited**: The target variable indicating whether the employee left the company (1 = Left, 0 = Stayed).

## Key Steps

1. **Exploratory Data Analysis (EDA)**:  
   - Performed analysis to understand the relationships between various features and the target variable (`Exited`).
   - Visualized data to detect patterns, correlations, and potential outliers.

2. **Data Preprocessing**:
   - Handled missing values and outliers.
   - Encoded categorical features (like `Gender` and `Geography`) using Label Encoding or One-Hot Encoding.
   - Scaled numerical features for training the neural network model.

3. **Model Development**:
   - Built an **Artificial Neural Network (ANN)** using **Keras** (with **TensorFlow** backend).
   - Trained the model using the processed data and validated it on the test set.
   - Evaluated the model performance with metrics such as **accuracy**, **precision**, and **recall**.

4. **Streamlit Web Application**:
   - Developed a **Streamlit** app to allow users to input employee data and predict if the employee is likely to stay or leave the company.
   - The app provides a simple interface where users can input values and get predictions in real time.

## Files Included

- `model.pkl`: The trained ANN model saved using **joblib**.
- `app.py`: Streamlit app script for model deployment.
- `eda.ipynb`: Jupyter notebook for performing exploratory data analysis.
- `train_model.py`: Python script to train the ANN model.
- `requirements.txt`: Python dependencies required for the project.

## Installation and Setup

Follow these steps to get the project up and running:

### Prerequisites

Make sure you have **Python 3.x** installed, and then install the required libraries.

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/employee-attrition-prediction.git
