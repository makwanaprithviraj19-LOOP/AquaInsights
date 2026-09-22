import streamlit as st

def render_chart_card(
    title: str,
    subtitle: str = "",
    action_label: str = "",
) -> None:
    action_html = f'<a href="#" style="font-size: 13px; font-weight: 500;">{action_label}</a>' if action_label else ""
    
    html = f"""
<div class="aqua-card">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
        <div>
            <div class="card-title" style="margin-bottom: 2px;">{title}</div>
            <div class="card-subtitle">{subtitle}</div>
        </div>
        {action_html}
    </div>
    <div style="height: 300px; border: 2px dashed #E5E5E5; border-radius: 8px; display: flex; align-items: center; justify-content: center; color: #9CA3AF; font-size: 14px; font-family: 'Inter', sans-serif;">
        Chart will be rendered here
    </div>
</div>
    """
    st.markdown(html, unsafe_allow_html=True)
