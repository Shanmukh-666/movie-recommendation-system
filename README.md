# Customer Churn Prediction System

## Overview

A Customer Churn Prediction System built using Machine Learning and Streamlit.

This project implements a supervised learning-based churn prediction system that predicts whether a customer will stay or leave a telecom service based on demographic, account, and usage information. The prediction engine uses XGBoost classifier to identify customers likely to churn and provides predictions through an interactive Streamlit web application.

---

## Features

- Predict whether a customer will stay or leave  
- Get real-time churn prediction  
- Machine learning-based classification  
- Interactive Streamlit interface  

---

## Technologies Used

- Python  
- Pandas  
- Scikit-Learn  
- XGBoost  
- Streamlit  

---

## Machine Learning Techniques

- Data Preprocessing  
- One-Hot Encoding  
- Feature Engineering  
- XGBoost Classifier  
- Train-Test Split  

---

## Dataset

Telco Customer Churn Dataset

https://www.kaggle.com/datasets/blastchar/telco-customer-churn  

---

## Project Structure

customer-churn-prediction/

app.py  
train_model.py  
model.pkl  
columns.pkl  
README.md  
data/Telco_customer_churn.xlsx  

---

## Run Project

Install dependencies and run commands:

```bash
uv add pandas scikit-learn xgboost streamlit joblib openpyxl
uv run python train_model.py
uv run streamlit run app.py
