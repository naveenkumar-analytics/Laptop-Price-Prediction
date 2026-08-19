# 💻 Laptop Price Predictor: End-to-End ML Web App

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **A production-ready Machine Learning web application that predicts laptop prices based on hardware specifications, built with Streamlit and deployed as a user-friendly interface.**

---

## 🚀 Project Overview

Manually estimating the fair market price of a laptop based on its configuration is time-consuming and subjective. This project solves that problem by leveraging **Machine Learning** to provide instant, data-driven price predictions.

**Key Business Impact:**
- ⚡ **Reduces estimation time** from minutes to milliseconds.
- 📊 **Removes human bias** by using historical market data.
- 🖥️ **Interactive UI** allows non-technical stakeholders (sales teams, buyers) to get predictions in real-time.

---

## 🧠 The Machine Learning Pipeline

This project follows a standard industry-grade ML pipeline:

1.  **Data Collection & Cleaning**: Handled missing values, outliers, and inconsistent categories.
2.  **Exploratory Data Analysis (EDA)**: Analyzed correlations between features (e.g., RAM, Processor, Brand) and the target variable (Price).
3.  **Feature Engineering**: Encoded categorical variables (One-Hot Encoding / Label Encoding) and scaled numerical features.
4.  **Model Training & Selection**: Experimented with multiple algorithms including:
    - Linear Regression
    - Decision Tree Regressor
    - Random Forest Regressor (Final Chosen Model 🏆)
    - XGBoost
5.  **Hyperparameter Tuning**: Used GridSearchCV / RandomizedSearchCV to optimize the final model.
6.  **Model Serialization**: Saved the trained pipeline using `pickle` (`.pkl` file) for seamless deployment.

---

## 🛠️ Tech Stack & Libraries

| Category | Technology |
| :--- | :--- |
| **Frontend / UI** | Streamlit |
| **Backend / ML** | Python, Scikit-learn, Pandas, NumPy |
| **Serialization** | Pickle / Joblib |
| **Visualization** | Matplotlib, Seaborn (for EDA) |
| **Environment** | Python 3.8+ |



## 📂 Dataset & Features

The model was trained on a comprehensive dataset of laptop specifications. Below are the key input features used for prediction:

| Feature | Type | Description |
| :--- | :--- | :--- |
| **Brand** | Categorical | Apple, Dell, HP, Lenovo, Asus, etc. |
| **Processor** | Categorical | Intel Core i3/i5/i7, AMD Ryzen 5/7, etc. |
| **RAM** | Numerical | Memory size in GB (e.g., 8GB, 16GB). |
| **Storage** | Numerical | Hard drive/SSD capacity in GB. |
| **Screen Size** | Numerical | Diagonal screen size in inches. |
| **Weight** | Numerical | Laptop weight in kg. |
| **OS** | Categorical | Windows, macOS, Linux, etc. |
| **GPU** | Categorical | NVIDIA, AMD, Integrated, etc. |
| **Target (Price)** | Numerical | The final price in INR/USD (Predicted). |

---

## 🏆 Model Performance

To ensure reliability, the model was evaluated using standard regression metrics:

| Metric | Score |
| :--- | :--- |
| **R² Score (Coefficient of Determination)** | 0.88 
| **Mean Absolute Error (MAE)** | .19


# 💻 Laptop Price Predictor: End-to-End ML Web App

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **A production-ready Machine Learning web application that predicts laptop prices based on hardware specifications, built with Streamlit and deployed as a user-friendly interface.**

---

## 🚀 Project Overview

Manually estimating the fair market price of a laptop based on its configuration is time-consuming and subjective. This project solves that problem by leveraging **Machine Learning** to provide instant, data-driven price predictions.

**Key Business Impact:**
- ⚡ **Reduces estimation time** from minutes to milliseconds.
- 📊 **Removes human bias** by using historical market data.
- 🖥️ **Interactive UI** allows non-technical stakeholders (sales teams, buyers) to get predictions in real-time.

---

## 🧠 The Machine Learning Pipeline

This project follows a standard industry-grade ML pipeline:

1.  **Data Collection & Cleaning**: Handled missing values, outliers, and inconsistent categories.
2.  **Exploratory Data Analysis (EDA)**: Analyzed correlations between features (e.g., RAM, Processor, Brand) and the target variable (Price).
3.  **Feature Engineering**: Encoded categorical variables (One-Hot Encoding / Label Encoding) and scaled numerical features.
4.  **Model Training & Selection**: Experimented with multiple algorithms including:
    - Linear Regression
    - Decision Tree Regressor
    - Random Forest Regressor (Final Chosen Model 🏆)
    - XGBoost
5.  **Hyperparameter Tuning**: Used GridSearchCV / RandomizedSearchCV to optimize the final model.
6.  **Model Serialization**: Saved the trained pipeline using `pickle` (`.pkl` file) for seamless deployment.

---

## 🛠️ Tech Stack & Libraries

| Category | Technology |
| :--- | :--- |
| **Frontend / UI** | Streamlit |
| **Backend / ML** | Python, Scikit-learn, Pandas, NumPy |
| **Serialization** | Pickle / Joblib |
| **Visualization** | Matplotlib, Seaborn (for EDA) |
| **Environment** | Python 3.8+ |


## 📂 Dataset & Features

The model was trained on a comprehensive dataset of laptop specifications. Below are the key input features used for prediction:

| Feature | Type | Description |
| :--- | :--- | :--- |
| **Brand** | Categorical | Apple, Dell, HP, Lenovo, Asus, etc. |
| **Processor** | Categorical | Intel Core i3/i5/i7, AMD Ryzen 5/7, etc. |
| **RAM** | Numerical | Memory size in GB (e.g., 8GB, 16GB). |
| **Storage** | Numerical | Hard drive/SSD capacity in GB. |
| **Screen Size** | Numerical | Diagonal screen size in inches. |
| **Weight** | Numerical | Laptop weight in kg. |
| **OS** | Categorical | Windows, macOS, Linux, etc. |
| **GPU** | Categorical | NVIDIA, AMD, Integrated, etc. |
| **Target (Price)** | Numerical | The final price in INR/USD (Predicted). |

---

## 🏆 Model Performance

To ensure reliability, the model was evaluated using standard regression metrics:

| Metric | Score |
| :--- | :--- |
| **R² Score (Coefficient of Determination)** | `0.92` *(Replace with your actual score)* |
| **Root Mean Squared Error (RMSE)** | `15,230` *(Replace with your actual error)* |
| **Mean Absolute Error (MAE)** | `10,450` *(Replace with your actual error)* |

*Note: The final model was chosen based on the highest R² score and lowest RMSE on the test set.*

---

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
