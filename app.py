import streamlit as st
import pickle
import numpy as np

# 1. Load the Model and Scaler
@st.cache_resource
def load_model():
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return scaler, model

scaler, model = load_model()

# 2. App Title and Description
st.title("🔥 Forest Fire Prediction App")
st.write("Enter the weather conditions below to predict if a forest fire is likely to occur.")

# 3. Create Input Fields
col1, col2 = st.columns(2)

with col1:
    # Region is vital! We map 0 -> Bejaia, 1 -> Sidi-Bel Abbes
    region = st.selectbox("Region", options=[0, 1], format_func=lambda x: "Bejaia (0)" if x == 0 else "Sidi-Bel Abbes (1)")
    temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=30.0)
    rh = st.number_input("Relative Humidity (%)", min_value=0.0, max_value=100.0, value=60.0)
    ws = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=50.0, value=15.0)

with col2:
    rain = st.number_input("Rain (mm)", min_value=0.0, max_value=50.0, value=0.0)
    ffmc = st.number_input("FFMC Index", min_value=0.0, max_value=100.0, value=80.0)
    dmc = st.number_input("DMC Index", min_value=0.0, max_value=200.0, value=20.0)
    isi = st.number_input("ISI Index", min_value=0.0, max_value=50.0, value=10.0)

# 4. Predict Button
if st.button("Predict Fire Risk"):
    try:
        # CRITICAL FIX: Order matches your X_train (Region is FIRST)
        features = np.array([[region, temperature, rh, ws, rain, ffmc, dmc, isi]])
        
        # Scale the data
        scaled_features = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(scaled_features)
        
        # EXTRACT THE NUMBER using [0]
        result_value = prediction[0]
        
        st.subheader("Prediction Result:")
        
        # Logic: Threshold at 0.5
        if result_value > 0.5:
            st.error(f"⚠️ FIRE LIKELY! (Score: {result_value:.4f})")
        else:
            st.success(f"✅ NO FIRE. (Score: {result_value:.4f})")
            
    except Exception as e:
        st.error(f"An error occurred: {e}")