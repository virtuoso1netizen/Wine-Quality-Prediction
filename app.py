import streamlit as st
import joblib
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Wine Quality Prediction",
    page_icon="🍷",
    layout="wide"
)

# Load Model
model = joblib.load("wine_quality_model.pkl")

# Custom CSS
st.markdown("""
<style>

.main {
    background-color: #f9f9f9;
}

h1{
    color:#7B1E3A;
}

.prediction-box{
    background:#f5f5f5;
    padding:20px;
    border-radius:15px;
    border-left:8px solid #7B1E3A;
}

</style>
""", unsafe_allow_html=True)

# Title
st.title("🍷 Wine Quality Prediction System")

st.markdown("""
Predict the **quality of Portuguese Red Wine**
using a **Random Forest Machine Learning Model**.
""")

st.divider()

# Sidebar
st.sidebar.header("📖 About")

st.sidebar.info("""
**Model Used**

Random Forest Classifier

**Dataset**

WineQT Dataset

1143 Samples

11 Features

Wine Quality Classes:
3 - 8
""")

# Input Section
st.subheader("Enter Wine Characteristics")

col1, col2 = st.columns(2)

with col1:

    fixed_acidity = st.slider("Fixed Acidity",4.0,16.0,7.4)

    volatile_acidity = st.slider("Volatile Acidity",0.10,1.60,0.70)

    citric_acid = st.slider("Citric Acid",0.00,1.00,0.00)

    residual_sugar = st.slider("Residual Sugar",0.5,16.0,2.2)

    chlorides = st.slider("Chlorides",0.01,0.70,0.07)

    free_sulfur = st.slider("Free Sulfur Dioxide",1,75,11)

with col2:

    total_sulfur = st.slider("Total Sulfur Dioxide",6,300,34)

    density = st.slider("Density",0.9900,1.0050,0.9978)

    ph = st.slider("pH",2.7,4.5,3.51)

    sulphates = st.slider("Sulphates",0.30,2.00,0.56)

    alcohol = st.slider("Alcohol",8.0,15.0,9.4)

# Prediction
if st.button("🍷 Predict Wine Quality", use_container_width=True):

    input_data = pd.DataFrame([[
        fixed_acidity,
        volatile_acidity,
        citric_acid,
        residual_sugar,
        chlorides,
        free_sulfur,
        total_sulfur,
        density,
        ph,
        sulphates,
        alcohol
    ]],
    columns=[
        'fixed acidity',
        'volatile acidity',
        'citric acid',
        'residual sugar',
        'chlorides',
        'free sulfur dioxide',
        'total sulfur dioxide',
        'density',
        'pH',
        'sulphates',
        'alcohol'
    ])

    prediction = model.predict(input_data)[0]

    if prediction <= 4:
        message = "🍋 Poor Quality Wine"

    elif prediction == 5:
        message = "🙂 Average Quality Wine"

    elif prediction == 6:
        message = "✅ Good Quality Wine"

    elif prediction == 7:
        message = "🌟 Very Good Quality Wine"

    else:
        message = "🏆 Excellent Quality Wine"

    st.markdown(f"""
    <div class="prediction-box">

    <h2>🍷 Predicted Quality : {prediction}</h2>

    <h3>{message}</h3>

    </div>
    """, unsafe_allow_html=True)

st.divider()

# Model Performance
st.subheader("Model Performance")

c1,c2,c3,c4 = st.columns(4)

c1.metric("Accuracy","70.31%")
c2.metric("Precision","66.87%")
c3.metric("Recall","70.31%")
c4.metric("F1 Score","68.17%")

st.divider()

st.caption("Developed by Anika Tyagi ❤️")
