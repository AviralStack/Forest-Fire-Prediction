import streamlit as st
import pickle
import numpy as np


@st.cache_resource
def load_model():
    
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return scaler, model

scaler, model = load_model()


st.set_page_config(page_title="Algerian Forest Fires Risk", page_icon="🌍")
st.title("🌍 Algerian Forest Fires Calculator")
st.markdown("Enter weather data to calculate the **Probability (%)** of a forest fire.")

st.sidebar.header("Weather Inputs")


region = st.sidebar.selectbox("Region Type", options=[0, 1], format_func=lambda x: "Bejaia (Humid)" if x == 0 else "Sidi-Bel Abbes (Dry)")

temperature = st.sidebar.slider("Temperature (°C)", 0, 50, 30)
rh = st.sidebar.slider("Relative Humidity (%)", 0, 100, 60)
ws = st.sidebar.slider("Wind Speed (km/h)", 0, 50, 15)
rain = st.sidebar.slider("Rain (mm)", 0.0, 50.0, 0.0)

st.sidebar.header("FWI Components")
ffmc = st.sidebar.slider("FFMC Index", 0.0, 100.0, 80.0)
dmc = st.sidebar.slider("DMC Index", 0.0, 200.0, 20.0)
isi = st.sidebar.slider("ISI Index", 0.0, 50.0, 10.0)


st.write("### 🔍 Live Analysis")

if st.button("Calculate Risk"):
    try:
        
        features = np.array([[region, temperature, rh, ws, rain, ffmc, dmc, isi]])
        
        scaled_features = scaler.transform(features)
        
        prob_array = model.predict_proba(scaled_features)
        fire_risk = prob_array[0][1] * 100  
        
       
        col1, col2 = st.columns(2)
        with col1:
            st.metric(label="🔥 Fire Probability", value=f"{fire_risk:.2f}%")
        
        
        st.progress(int(fire_risk))
        
        if fire_risk > 75:
            st.error("🚨 EXTREME DANGER! High probability of fire.")
        elif fire_risk > 40:
            st.warning("⚠️ MODERATE RISK. Conditions are dangerous.")
        else:
            st.success("✅ LOW RISK. Conditions are safe.")
            
    except Exception as e:
        st.error(f"Error: {e}")