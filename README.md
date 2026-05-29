# House Price Prediction

A complete end-to-end data science project that predicts house prices 
based on various features such as overall quality, living area, garage 
capacity, and more. Built using Python, Scikit-learn, and Streamlit.

---

## Project Overview

This project follows the complete data science workflow:

1. Data Collection and Exploration
2. Data Cleaning and Transformation
3. Exploratory Data Analysis
4. Feature Selection
5. Model Development
6. Model Evaluation and Hyperparameter Tuning
7. Streamlit Web Application

---

## Dataset

The dataset is sourced from the Kaggle House Prices competition.
It contains 1460 rows and 81 columns describing various features 
of residential homes in Ames, Iowa.

Dataset link: https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques

---

## Technologies Used

- Python 3.13
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Joblib

---

## Project Structure
DS Certification Task/
│
├── house_price_prediction.ipynb   # Main Jupyter Notebook
├── app.py                         # Streamlit web application
├── run_app.bat                    # Run the app on Windows
├── train.csv                      # Dataset
├── model.pkl                      # Saved trained model
├── scaler.pkl                     # Saved StandardScaler
├── feature_names.pkl              # Saved feature names
├── feature_means.pkl              # Saved feature means
└── README.md                      # Project documentation

---

## Model Performance

| Model | MAE | RMSE | R2 Score |
|---|---|---|---|
| Linear Regression | 0.0917 | 0.1274 | 0.8972 |
| Random Forest | 0.1051 | 0.1537 | 0.8505 |
| Gradient Boosting | 0.0951 | 0.1359 | 0.8831 |
| Gradient Boosting Tuned | 0.0939 | 0.1349 | 0.8848 |

Linear Regression was selected as the final model with an R2 score 
of 0.8972.

---

## How to Run the App

### Option 1: Windows (double click)
1. Double click run_app.bat
2. The app will open in your browser at http://localhost:8501

### Option 2: Terminal
1. Clone the repository
2. Install the required libraries:
   pip install pandas numpy matplotlib seaborn scikit-learn streamlit joblib
3. Run the app:
   streamlit run app.py
4. The app will open in your browser at http://localhost:8501

## Author

Sweta Khadka
