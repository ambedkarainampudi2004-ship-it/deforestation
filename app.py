import streamlit as st
import numpy as np
import pickle
import time

# ================= LOAD MODEL =================
model = pickle.load(open("model.pkl", "rb"))

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="🔥 Forest Fire Prediction System",
    page_icon="🔥",
    layout="wide"
)

# ================= CSS =================
st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #0b3d0b,
        #2e8b57,
        #556b2f,
        #f1c40f
    );
}

.main-title{
    text-align:center;
    font-size:50px;
    font-weight:bold;
    color:white;
}

.sub-title{
    text-align:center;
    color:white;
    font-size:18px;
}

.result-box{
    padding:20px;
    border-radius:20px;
    background:rgba(255,255,255,0.15);
    backdrop-filter:blur(10px);
}

</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown(
    "<h1 class='main-title'>🔥 AI Forest Fire Prediction System</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p class='sub-title'>Predict Forest Fire Risk using Environmental Conditions</p>",
    unsafe_allow_html=True
)

st.divider()

# ================= INPUTS =================
col1, col2 = st.columns(2)

with col1:

    Temperature = st.number_input(
        "🌡 Temperature (°C)",
        value=32.0
    )

    RH = st.number_input(
        "💧 Relative Humidity (%)",
        value=60.0
    )

    Ws = st.number_input(
        "🌬 Wind Speed",
        value=15.0
    )

    Rain = st.number_input(
        "🌧 Rainfall",
        value=0.0
    )

    FFMC = st.number_input(
        "🔥 FFMC",
        value=85.0
    )

with col2:

    DMC = st.number_input(
        "🌲 DMC",
        value=20.0
    )

    DC = st.number_input(
        "☀ DC",
        value=60.0
    )

    ISI = st.number_input(
        "⚡ ISI",
        value=5.0
    )

    BUI = st.number_input(
        "🌳 BUI",
        value=20.0
    )

    FWI = st.number_input(
        "🔥 FWI",
        value=5.0
    )

# ================= BUTTON =================
if st.button("🚀 Predict Fire Risk"):

    with st.spinner("Analyzing forest conditions..."):
        time.sleep(2)

        data = np.array([[
            Temperature,
            RH,
            Ws,
            Rain,
            FFMC,
            DMC,
            DC,
            ISI,
            BUI,
            FWI
        ]])

        prediction = model.predict(data)[0]
        probability = model.predict_proba(data)[0]

    st.success("Analysis Completed!")

    # IMPORTANT:
    # Class 0 = FIRE
    # Class 1 = NOT FIRE

    fire_prob = probability[0] * 100
    safe_prob = probability[1] * 100

    st.markdown("<div class='result-box'>", unsafe_allow_html=True)

    if prediction == 0:

        st.error("🔥 HIGH FIRE RISK DETECTED")

    else:

        st.success("🌲 NO FIRE RISK DETECTED")

    st.metric(
        label="🔥 Fire Probability",
        value=f"{fire_prob:.2f}%"
    )

    st.metric(
        label="🌲 Safe Probability",
        value=f"{safe_prob:.2f}%"
    )

    st.markdown("</div>", unsafe_allow_html=True)