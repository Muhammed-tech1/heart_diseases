import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load("heart_diseases_model.pickle")  

# Background CSS with hospital image
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://images.unsplash.com/photo-1588776814546-ec7ffbcbf1b7?auto=format&fit=crop&w=1470&q=80');
        background-size: cover;
        background-attachment: fixed;
    }
    .block-container {
        background-color: rgba(0, 0, 0, 0.7);
        padding: 2rem;
        border-radius: 12px;
    }
    h1, h3 {
        color: #00ffff;
    }
    .stButton>button {
        background-color: #00ffff;
        color: black;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="block-container">', unsafe_allow_html=True)

# Title
st.title("🏥 Heart Disease Death Event Prediction")
st.markdown("### 📝 Enter the patient's health details:")

# Input Fields (13 total)
age = st.slider("Age", 0, 100, 50)
anaemia = st.selectbox("Anaemia (0 = No, 1 = Yes)", [0, 1])
creatinine_phosphokinase = st.number_input("Creatinine Phosphokinase", 0)
diabetes = st.selectbox("Diabetes", [0, 1])
ejection_fraction = st.slider("Ejection Fraction (%)", 0, 100, 50)
high_blood_pressure = st.selectbox("High Blood Pressure", [0, 1])
platelets = st.number_input("Platelets (kiloplatelets/mL)", 0.0)
serum_creatinine = st.number_input("Serum Creatinine (mg/dL)", 0.0)
serum_sodium = st.number_input("Serum Sodium (mEq/L)", 0.0)
sex = st.selectbox("Sex", ["Female", "Male"])
sex = 1 if sex == "Male" else 0
smoking = st.selectbox("Smoking", [0, 1])
time = st.slider("Follow-up Period (Days)", 0, 500, 100)

# New Column: age_group (select manually to match trained model)
age_group = st.selectbox("Age Group", [
    "0-10", "11-20", "21-30", "31-40", "41-50",
    "51-60", "61-70", "71-80", "81-90", "91-100"
])

# Convert categorical age_group to numeric using label encoding (or your trained format)
# You must match how you encoded age_group during training
age_group_dict = {
    "0-10": 0, "11-20": 1, "21-30": 2, "31-40": 3, "41-50": 4,
    "51-60": 5, "61-70": 6, "71-80": 7, "81-90": 8, "91-100": 9
}
age_group_encoded = age_group_dict[age_group]

# Predict button
if st.button("🔍 Predict Death Event"):
    input_data = np.array([[age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction,
                            high_blood_pressure, platelets, serum_creatinine, serum_sodium,
                            sex, smoking, time, age_group_encoded]])
    
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk: Death Event Likely")
    else:
        st.success("✅ Low Risk: Death Event Unlikely")

st.markdown('</div>', unsafe_allow_html=True)