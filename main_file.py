import streamlit as st
import numpy as np
import joblib

# Load the trained model
with open('MLassignment2.pkl', 'rb') as file:
    model = joblib.load(file)

# Streamlit UI
st.set_page_config(page_title="Verification Prediction", page_icon="☁️", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to top, #ffffff, #87CEEB);
        }
        body {
            background-color: #87CEEB; /* Sky Blue */
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 10px;
        }
        .stSuccess {
            font-size: 22px;
            font-weight: bold;
            color: green;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔍 Verification Result Prediction _ for CI")
st.write("Fill in the details below and click **Predict** to get the result.")

# Input fields for user to enter values
process_b1_capacity = st.number_input("Process B1 Capacity", value=0)
process_b2_capacity = st.number_input("Process B2 Capacity", value=0)
process_b3_capacity = st.number_input("Process B3 Capacity", value=0)
process_b4_capacity = st.number_input("Process B4 Capacity", value=0)
property_price = st.number_input("Property Price", value=0)
property_product = st.number_input("Property Product", value=0)
property_winner = st.number_input("Property Winner", value=0)
verification_time = st.number_input("Verification Time", value=0.00)

# Predict button
if st.button("🚀 Predict"):
    # Prepare input data
    user_input = np.array([[
        process_b1_capacity, process_b2_capacity, process_b3_capacity,
        process_b4_capacity, property_price, property_product,
        property_winner, verification_time
    ]])

    # Make prediction
    prediction = model.predict(user_input)

    # Convert to boolean
    prediction_bool = bool(prediction[0])

    # Display result
    if prediction_bool:
        st.success("✅ **Verification Passed!**")
    else:

        st.success("❌ **Verification Failed!**")
