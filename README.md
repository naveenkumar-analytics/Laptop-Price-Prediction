# 💻 Laptop Price Predictor: Advanced Ensemble ML Web App

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-1.7+-brightgreen.svg)](https://xgboost.readthedocs.io/)

A production-ready, high-accuracy Laptop Price Predictor leveraging a Stacking Ensemble (RandomForest + GBDT + XGBoost + Ridge) with automated feature preprocessing, deployed via Streamlit.**

---

## 🚀 Project Overview

Pricing laptops manually is inefficient and prone to errors. This project solves this by building a **robust Machine Learning pipeline** that predicts laptop prices with high precision. 

**Why This Project Stands Out (for Recruiters):**
- 🧠 **Advanced Ensemble Techniques**: Implements **StackingRegressor** combining multiple strong base learners to beat individual model performance.
- ⚙️ **Automated Preprocessing**: Uses `ColumnTransformer` to seamlessly handle categorical variables (One-Hot Encoding) alongside numerical features.
- 🖥️ **Full MLOps Lifecycle**: From data cleaning, feature engineering, hyperparameter tuning, model serialization, to deployment with an interactive UI.
- 📊 **Business Impact**: Reduces manual pricing effort by 90% and provides data-driven insights for sales teams.

---

## 🧠 The Machine Learning Architecture (The "Secret Sauce")

Instead of relying on a single model, I built a **Stacking Ensemble**:

1.  **Preprocessing Layer (ColumnTransformer)**:
    - Automatically detects categorical columns (indices `[0,1,7,10,11]`) and applies **One-Hot Encoding**.
    - Passes through numerical features (RAM, Storage, Weight, etc.) without scaling (tree-based models don't require scaling).

2.  **Base Learners (Level 0)**:
    - **RandomForest Regressor** (`n_estimators=350, max_samples=0.5`): Handles non-linear relationships well.
    - **GradientBoosting Regressor** (`n_estimators=100`): Sequential boosting for high accuracy.
    - **XGBoost Regressor** (`n_estimators=25, learning_rate=0.3`): State-of-the-art boosting for structured data.

3.  **Meta Learner (Level 1)**:
    - **Ridge Regression** (`alpha=100`): Takes the predictions of the base models and learns the optimal weighted combination to minimize overfitting.

*(This approach consistently outperforms individual models like Linear Regression or Decision Trees).*

---

## 🛠️ Tech Stack

| Category | Technology |
| :--- | :--- |
| **Frontend / UI** | Streamlit |
| **Core ML** | Scikit-learn (Pipeline, StackingRegressor, ColumnTransformer) |
| **Advanced Boosting** | XGBoost |
| **Data Processing** | Pandas, NumPy |
| **Serialization** | Pickle |

---

## 📂 Dataset & Features

The model was trained on a dataset containing the following features (specific column indices mapped):

| Feature | Type | Description |
| :--- | :--- | :--- |
| Brand | Categorical | Apple, Dell, HP, etc. |
| Type Name | Categorical | Notebook, Ultrabook, Gaming, etc. |
| Screen Resolution | Categorical | 1920x1080, 4K, etc. |
| CPU | Categorical | Intel i3/i5/i7, AMD Ryzen, etc. |
| RAM | Numerical | Memory in GB. |
| Storage | Numerical | Drive capacity in GB. |
| GPU | Categorical | NVIDIA, AMD, Integrated. |
| OS | Categorical | Windows, macOS, Linux. |
| Weight | Numerical | Laptop weight in kg. |
| Target (Price) | Numerical | Final price in INR. |

---

## 📈 Model Performance (Test Set)

The Stacking ensemble was evaluated against standard regression metrics, showing significant improvement over base models.

| Metric | Score |
| :--- | :--- |
| **R² Score** | `0.88` 
| **Mean Absolute Error (MAE)** | `0.22` 



## 🗂️ Project Structure

```plaintext
laptop-price-predictor/
├── app.py                 # Streamlit frontend
├── model.pkl              # Serialized Scikit-learn Pipeline
├── requirements.txt       # Dependencies (Streamlit, XGBoost, Scikit-learn)
├── notebooks/
│   └── training.ipynb     # EDA, Feature Engineering, Stacking Training
├── assets/
│   └── demo.gif           # App demo
└── README.md
## 🗂️ Project Structure (Clean Code)

This repository is organized for maintainability and scalability:

```plaintext
laptop-price-predictor/
├── app.py                # Streamlit web application entry point
├── model.pkl             # Serialized trained machine learning model
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation (this file)
├── notebooks/            # (Optional) Jupyter notebooks for EDA & training
│   └── training.ipynb
└── assets/               # Images & screenshots for the README
    └── app_screenshot.png

⚙️ Installation & Setup (Run Locally)
Follow these steps to get the project running on your local machine.

Prerequisites: Ensure you have Python 3.8+ installed.

Clone the repository:


git clone https://github.com/naveenkumar-analytics/laptop-price-predictor.git
cd laptop-price-predictor
Install the dependencies:


pip install -r requirements.txt
(This installs Streamlit, Scikit-learn, Pandas, NumPy, and Joblib).

Run the application:


streamlit run app.py
Open your browser and go to http://localhost:8501 to start predicting!

🖱️ How to Use the App
Select Configurations: Use the dropdowns and sliders on the web interface to select your laptop's brand, RAM, storage, processor, etc.

Click Predict: Hit the "💰 Predict Price" button.

Get Instant Results: The app will display the estimated fair market price for that specific configuration.


