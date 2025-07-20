🫀 Heart Disease Prediction with Machine Learning

This project is a machine learning-based web application that predicts the risk of death in patients with heart failure using clinical records. It was built with Scikit-learn, Joblib, and Streamlit, and deployed as an interactive web app with a hospital-themed design.
🚀 Demo

You can run the app locally with:

streamlit run heart_disease_model.py

📊 Features Used

The model was trained on 13 key features:

    age – Age of the patient (in years)

    anaemia – Decrease of red blood cells or hemoglobin (1 = Yes, 0 = No)

    creatinine_phosphokinase – Level of the CPK enzyme in the blood

    diabetes – Whether the patient has diabetes (1 = Yes, 0 = No)

    ejection_fraction – Percentage of blood leaving the heart at each contraction

    high_blood_pressure – Whether the patient has hypertension

    platelets – Platelet count in the blood

    serum_creatinine – Level of creatinine in the blood

    serum_sodium – Level of sodium in the blood

    sex – Gender (1 = Male, 0 = Female)

    smoking – Whether the patient smokes (1 = Yes, 0 = No)

    time – Follow-up period (in days)

    age_group – Grouped age category (encoded as integers)

🎯 Target Variable

    DEATH_EVENT – Whether the patient died during the follow-up period (1 = Yes, 0 = No)

🧠 Model & Training

    Model Used: Logistic Regression

    Data Preprocessing: Label encoding was applied to categorical features like sex, smoking, and age_group.

    Frameworks: Scikit-learn for model training, Joblib for model saving/loading.

🌐 Web App Details

    Built using Streamlit for easy deployment and interactivity.

    Includes a user-friendly interface for entering patient data.

    Custom background image of a hospital scene to match the medical theme.

    Predicts whether a patient is at high or low risk of death based on clinical data.

📁 Files Included

    heart_disease_model.py – Streamlit application file

    Model – Trained logistic regression model

    README.md – Project documentation

🙋‍♂️ Author

    Name: Muhammed Abdullahi

    GitHub: Muhammed-tech1
    Email: abdulmuhammed284@gmail.com
    phone: +2347o17179687
    
