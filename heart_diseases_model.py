import pandas as pandas
import numpy as np
import joblib
import streamlit as st



# Load model
model = joblib.load("model.pkl")  # Replace with your actual model path

# Add background image using base64
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1615461066841-1b8d39468a07?auto=format&fit=crop&w=1470&q=80");
             background-attachment: fixed;
             background-size: cover;
             color: white;
         }}
         h1, h2, h3, h4 {{
             color: #00ffff;
         }}
         .stButton>button {{
             background-color: #00ffff;
             color: black;
             font-weight: bold;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

# App Title
st.title("💓 Heart Disease Death Event Prediction")

st.markdown("### 📝 Enter the patient's details below:")

# Input Widgets
age = st.slider("Age", 0, 100, 50)
anaemia = st.selectbox("Anaemia", [0, 1])
creatinine_phosphokinase = st.number_input("Creatinine Phosphokinase", 0)
diabetes = st.selectbox("Diabetes", [0, 1])
ejection_fraction = st.slider("Ejection Fraction", 0, 100, 50)
high_blood_pressure = st.selectbox("High Blood Pressure", [0, 1])
platelets = st.number_input("Platelets (kiloplatelets/mL)", 0.0)
serum_creatinine = st.number_input("Serum Creatinine (mg/dL)", 0.0)
serum_sodium = st.number_input("Serum Sodium (mEq/L)", 0.0)
sex = st.selectbox("Sex", ["Female", "Male"])
sex = 1 if sex == "Male" else 0
smoking = st.selectbox("Smoking", [0, 1])
time = st.slider("Follow-up Period (Days)", 0, 500, 100)

# Predict Button
if st.button("🔍 Predict Death Event"):
    input_data = np.array([[age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction,
                            high_blood_pressure, platelets, serum_creatinine, serum_sodium,
                            sex, smoking, time]])
    
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ High risk: Death event likely.")
    else:
        st.success("✅ Low risk: Death event not likely.")