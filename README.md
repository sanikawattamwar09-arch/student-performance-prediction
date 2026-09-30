# Student Performance Prediction

## 📌 Project Overview

Student Performance Prediction is a beginner-friendly machine learning project that predicts whether a student is likely to pass or fail based on study hours, attendance, previous score, and completed assignments.

The project uses Logistic Regression for binary classification.

## 🎯 Objective

The main objective of this project is to understand the basic machine learning workflow:

- Data loading
- Data checking
- Feature selection
- Train-test splitting
- Model training
- Prediction
- Model evaluation

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib

## 📊 Dataset

The dataset contains the following features:

| Feature | Description |
|---|---|
| study_hours | Number of hours studied |
| attendance | Attendance percentage |
| previous_score | Previous exam score |
| assignments_completed | Number of completed assignments |
| result | Target variable |

The target variable is:

- `0` = Fail
- `1` = Pass

## 🤖 Machine Learning Algorithm

### Logistic Regression

Logistic Regression is used because this project is a binary classification problem.

The model predicts one of two outcomes:

- Pass
- Fail

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Checking
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Logistic Regression
   ↓
Model Training
   ↓
Prediction
   ↓
Model Evaluation