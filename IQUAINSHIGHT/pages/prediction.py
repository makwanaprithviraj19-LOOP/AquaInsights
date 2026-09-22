"""
AquaInsights — Water Potability Prediction Page
Machine learning inference model form & potability result card matching Image 1 (#12 Prediction).
"""

import streamlit as st
from services.prediction_engine import PredictionEngine

def render() -> None:
    pred_engine = PredictionEngine()

    st.markdown('<div class="card-title" style="font-size: 18px; margin-bottom: 16px;">Water Potability Machine Learning Prediction</div>', unsafe_allow_html=True)

    col_inputs, col_result = st.columns([1.5, 1.5])

    with col_inputs:
        with st.container(border=True):
            st.markdown('### Input Parameters')

            ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.18, step=0.1)
            hardness = st.number_input("Hardness (mg/L)", min_value=0.0, value=195.0, step=5.0)
            solids = st.number_input("Solids / TDS (ppm)", min_value=0.0, value=20500.0, step=100.0)
            chloramines = st.number_input("Chloramines (ppm)", min_value=0.0, value=7.1, step=0.1)
            sulfate = st.number_input("Sulfate (mg/L)", min_value=0.0, value=333.0, step=5.0)
            conductivity = st.number_input("Conductivity (µS/cm)", min_value=0.0, value=420.0, step=10.0)
            organic_carbon = st.number_input("Organic Carbon (ppm)", min_value=0.0, value=14.3, step=0.5)
            trihalomethanes = st.number_input("Trihalomethanes (µg/L)", min_value=0.0, value=66.4, step=1.0)
            turbidity = st.number_input("Turbidity (NTU)", min_value=0.0, value=2.1, step=0.1)

            features = {
                'pH': ph,
                'Hardness': hardness,
                'Solids': solids,
                'Chloramines': chloramines,
                'Sulfate': sulfate,
                'Conductivity': conductivity,
                'Organic_Carbon': organic_carbon,
                'Trihalomethanes': trihalomethanes,
                'Turbidity': turbidity
            }

            st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
            predict_btn = st.button("🧠 Predict Water Potability", key="btn_run_pred", type="primary", use_container_width=True)

    with col_result:
        res = pred_engine.predict(features)

        st.markdown(
            f"""
<div class="aqua-card" style="padding: 30px; text-align: center; min-height: 480px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
    <div class="card-subtitle" style="text-transform: uppercase; letter-spacing: 1px;">Prediction Result</div>
    
    <div style="margin: 24px 0;">
        <div style="width: 120px; height: 120px; border-radius: 50%; background: {"rgba(34,197,94,0.15)" if res['is_potable'] else "rgba(239,68,68,0.15)"}; display: inline-flex; align-items: center; justify-content: center;">
            <span style="font-size: 54px;">{"💧" if res['is_potable'] else "⚠️"}</span>
        </div>
    </div>

    <div style="font-size: 24px; font-weight: 800; color: {res['color']}; margin-bottom: 8px;">
        {res['status']}
    </div>

    <div style="font-size: 13px; color: #6B7280; max-width: 320px; line-height: 1.5; margin-bottom: 24px;">
        {res['description']}
    </div>

    <div style="background: #F8FAFC; border: 1px solid #E5E5E5; padding: 12px 24px; border-radius: 10px;">
        <div style="font-size: 11px; color: #6B7280; font-weight: 600;">CONFIDENCE SCORE</div>
        <div style="font-size: 24px; font-weight: 800; color: #111827;">{res['confidence']}%</div>
    </div>
</div>
            """,
            unsafe_allow_html=True
        )
