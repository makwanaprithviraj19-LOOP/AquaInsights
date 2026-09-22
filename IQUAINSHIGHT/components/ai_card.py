import streamlit as st

def render_ai_card(
    title: str = "AI Quick Insights",
    insights: list[str] | None = None,
) -> None:
    """Render an AI insight card component."""
    if insights is None:
        insights = [
            "Average pH (7.18) is within WHO recommended drinking water standards (6.5 – 8.5).",
            "Water quality appears healthy overall with an estimated 88.7% safe water compliance rate.",
            "Conductivity shows strong positive correlation (+0.68) with Total Dissolved Solids (TDS).",
            "Turbidity levels average 2.1 NTU, well within the acceptable maximum limit of 5.0 NTU.",
            "No significant parameter abnormalities or toxic contamination spikes detected in the dataset."
        ]

    items_html = ""
    for insight in insights:
        items_html += f'<li style="display: flex; gap: 10px; margin-bottom: 12px; font-family: Inter, sans-serif; font-size: 13px; color: #4B5563;"><span style="color: #22C55E; font-weight: bold;">✔</span><span>{insight}</span></li>'

    html = f"""
<div class="aqua-card" style="padding: 20px;">
    <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 16px;">
        <span style="font-size: 18px; color: #7C3AED;">✨</span>
        <div class="card-title" style="margin: 0; color: #111827;">{title}</div>
    </div>
    <ul style="list-style: none; padding: 0; margin: 0;">
        {items_html}
    </ul>
    <div style="margin-top: 16px; text-align: right;">
        <a href="#" style="font-family: Inter, sans-serif; font-size: 12px; font-weight: 500; color: #1E88E5; text-decoration: none;">
            View All Insights &rarr;
        </a>
    </div>
</div>
    """
    st.markdown(html, unsafe_allow_html=True)
