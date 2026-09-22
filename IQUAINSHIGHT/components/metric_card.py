import streamlit as st
from utils.colors import Colors

def render_metric_card(
    title: str,
    value: str,
    subtitle: str = "",
    icon: str = "",
    trend: str = "",
    trend_direction: str = "up",
    color: str = "#1E88E5",
) -> None:
    trend_color = Colors.SUCCESS if trend_direction == "up" else Colors.DANGER
    trend_arrow = "↑" if trend_direction == "up" else "↓"
    trend_html = f'<span style="color: {trend_color}; font-size: 12px; font-weight: 600;">{trend_arrow} {trend}</span>' if trend else ""

    html = f"""
<div class="aqua-card" style="display: flex; flex-direction: column; gap: 12px;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div style="width: 40px; height: 40px; border-radius: 50%; background-color: {color}20; display: flex; align-items: center; justify-content: center; color: {color}; font-size: 20px;">
            {icon}
        </div>
        {trend_html}
    </div>
    <div>
        <div class="metric-value">{value}</div>
        <div class="card-title" style="margin-bottom: 2px;">{title}</div>
        <div class="card-subtitle">{subtitle}</div>
    </div>
</div>
    """
    st.markdown(html, unsafe_allow_html=True)
