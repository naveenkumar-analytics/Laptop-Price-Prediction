import streamlit as st
import pickle
import pandas as pd

# Load trained model
with open("model.pkl", "rb") as file:
    pipe = pickle.load(file)


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Laptop Price Predictor")
st.write("Enter the laptop details to predict its price.")


# -----------------------------
# Get categorical values
# directly from trained encoder
# -----------------------------

encoder = pipe.named_steps["step1"].transformers_[0][1]

categories = encoder.categories_

company_options = categories[0]
typename_options = categories[1]
cpu_options = categories[2]
gpu_options = categories[3]
os_options = categories[4]


# -----------------------------
# UI
# -----------------------------

col1, col2 = st.columns(2)


with col1:

    company = st.selectbox(
        "Company",
        company_options
    )

    typename = st.selectbox(
        "Type",
        typename_options
    )

    ram = st.number_input(
        "RAM (GB)",
        min_value=1,
        max_value=64,
        value=8,
        step=1
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=0.5,
        max_value=10.0,
        value=2.0,
        step=0.1
    )

    touchscreen = st.selectbox(
        "Touchscreen",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )

    ips = st.selectbox(
        "IPS Display",
        [0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )


with col2:

    ppi = st.number_input(
        "PPI",
        min_value=50.0,
        max_value=500.0,
        value=150.0,
        step=1.0
    )

    cpu = st.selectbox(
        "CPU Brand",
        cpu_options
    )

    hdd = st.number_input(
        "HDD (GB)",
        min_value=0,
        max_value=4000,
        value=0,
        step=128
    )

    ssd = st.number_input(
        "SSD (GB)",
        min_value=0,
        max_value=2000,
        value=256,
        step=128
    )

    gpu = st.selectbox(
        "GPU Brand",
        gpu_options
    )

    os = st.selectbox(
        "Operating System",
        os_options
    )


# -----------------------------
# Prediction
# -----------------------------

# -----------------------------
# Prediction
# -----------------------------

if st.button("🔮 Predict Price", use_container_width=True):

    input_data = pd.DataFrame({
        "Company": [company],
        "TypeName": [typename],
        "Ram": [ram],
        "Weight": [weight],
        "Touchscreen": [touchscreen],
        "Ips": [ips],
        "ppi": [ppi],
        "Cpu brand": [cpu],
        "HDD": [hdd],
        "SSD": [ssd],
        "Gpu brand": [gpu],
        "os": [os]
    })


    import numpy as np

    prediction = pipe.predict(input_data)

    actual_price = np.exp(prediction[0])

    st.success(
        f"💰 Predicted Price: ₹ {actual_price:,.2f} Rupees"
    )