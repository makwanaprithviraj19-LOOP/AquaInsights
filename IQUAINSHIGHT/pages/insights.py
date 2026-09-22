"""
AquaInsights — AI Insights Page
AI insights list & interactive data chat assistant matching Image 1 (#11 AI Insights).
"""

import streamlit as st
from services.ai_engine import AIEngine
from services.csv_loader import CSVLoader

def render() -> None:
    loader = CSVLoader()
    ai = AIEngine()
    df = loader.get_default_dataset()

    with st.container(border=True):
        st.markdown(
            """
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <div style="display: flex; align-items: center; gap: 8px;">
                        <span style="font-size: 20px; color: #7C3AED;">✨</span>
                        <span class="card-title" style="font-size: 18px; margin: 0;">AI Insights</span>
                    </div>
                    <div class="card-subtitle" style="margin-top: 4px;">Get AI-powered insights about your dataset</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
    
    if st.button("✨ Analyze this water quality dataset and give me insights", key="btn_gen_ai_insights", type="primary", use_container_width=True):
        st.toast("Generated fresh AI Insights!")

    st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)

    # ── Insights List Card ───────────────────────────────────────────────────
    with st.container(border=True):
        st.markdown('<div><b>Based on key analysis of your dataset, here are the key insights:</b></div>', unsafe_allow_html=True)
        st.markdown('<div style="height: 12px;"></div>', unsafe_allow_html=True)

        insights_list = ai.generate_insights(df)
        for insight in insights_list:
            st.markdown(
                f"""
    <div style="display: flex; align-items: flex-start; gap: 10px; margin-bottom: 10px; font-size: 13px; color: #111827;">
        <span style="color: #1E88E5; font-size: 14px;">•</span>
        <span>{insight}</span>
    </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("<div style='height: 20px;'></div>", unsafe_allow_html=True)

    # ── Interactive Chat Section ─────────────────────────────────────────────
    with st.container(border=True):
        st.markdown('### Ask anything about your data...')

        user_query = st.text_input("", placeholder="e.g., Is pH level within WHO limit?", key="ai_chat_input")
        if user_query:
            ans = ai.answer_question(df, user_query)
            st.markdown(
                f"""
    <div style="background: #F8FAFC; border: 1px solid #E5E5E5; border-radius: 8px; padding: 14px; margin-top: 12px;">
        <div style="font-size: 11px; font-weight: 600; color: #1E88E5; margin-bottom: 4px;">AQUAINSIGHTS AI ASSISTANT</div>
        <div style="font-size: 13px; color: #111827; line-height: 1.5;">{ans}</div>
    </div>
                """,
                unsafe_allow_html=True
            )
