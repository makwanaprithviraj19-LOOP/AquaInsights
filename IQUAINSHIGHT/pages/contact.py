"""
AquaInsights — Contact Us Page
Split layout with contact info (left) and form (right).
"""

import streamlit as st


def render() -> None:
    """Render the Contact Us page."""

    st.markdown(_contact_css(), unsafe_allow_html=True)

    # ── Page Header ───────────────────────────────────────────────────────
    st.markdown(_contact_header_html(), unsafe_allow_html=True)

    left, right = st.columns([1, 1.2], gap="large")

    # ═══════════════════ LEFT — Contact Information ═══════════════════════
    with left:
        st.markdown(_contact_info_html(), unsafe_allow_html=True)

    # ═══════════════════ RIGHT — Contact Form ════════════════════════════
    with right:
        st.markdown(_contact_form_header_html(), unsafe_allow_html=True)

        with st.form("contact_form_main", clear_on_submit=True):
            name = st.text_input("Full Name", placeholder="John Doe", key="contact_name")
            email = st.text_input("Email Address", placeholder="you@example.com", key="contact_email")
            subject = st.text_input("Subject", placeholder="Question about AquaInsights", key="contact_subject")
            message = st.text_area("Message", placeholder="Write your message here...", height=120, key="contact_message")

            submitted = st.form_submit_button("Send Message ✉️", type="primary", use_container_width=True)

            if submitted:
                if name and email and message:
                    st.success(f"Thank you, {name}! Your message has been received. We will respond within 24 hours.")
                    st.balloons()
                else:
                    st.warning("Please fill in all required fields (Name, Email, Message).")


def _contact_header_html() -> str:
    return """<div style="text-align:center; padding:8px 0 24px 0;">
<div class="contact-badge">Get In Touch</div>
<h1 class="contact-heading">Contact Us</h1>
<p class="contact-sub">Have questions about AquaInsights? We would love to hear from you.</p>
</div>"""


def _contact_info_html() -> str:
    return """<div class="contact-info-card">
<h3 class="ci-title">Contact Information</h3>
<p class="ci-subtitle">Reach out through any of the channels below.</p>
<div class="ci-row"><div class="ci-icon-wrap"><span class="ci-icon">🏫</span></div><div><div class="ci-label">Institution</div><div class="ci-value">Department of Computer Science</div></div></div>
<div class="ci-row"><div class="ci-icon-wrap"><span class="ci-icon">📍</span></div><div><div class="ci-label">Location</div><div class="ci-value">University Campus, City, State 000000</div></div></div>
<div class="ci-row"><div class="ci-icon-wrap"><span class="ci-icon">✉️</span></div><div><div class="ci-label">Email</div><div class="ci-value">contact@aquainsights.io</div></div></div>
<div class="ci-row"><div class="ci-icon-wrap"><span class="ci-icon">📞</span></div><div><div class="ci-label">Phone</div><div class="ci-value">+91 98765 43210</div></div></div>
<div class="ci-row"><div class="ci-icon-wrap"><span class="ci-icon">🕒</span></div><div><div class="ci-label">Working Hours</div><div class="ci-value">Mon – Fri, 9 AM – 6 PM IST</div></div></div>
</div>"""


def _contact_form_header_html() -> str:
    return """<div style="margin-bottom:12px;">
<h3 style="font-family:'Poppins',sans-serif; font-size:17px; font-weight:600; color:#111827; margin:0 0 2px 0;">Send a Message</h3>
<p style="font-family:'Inter',sans-serif; font-size:12px; color:#6B7280; margin:0;">Fill in the form and we will get back to you within 24 hours.</p>
</div>"""


def _contact_css() -> str:
    return """<style>
.contact-badge {
    display:inline-block; font-family:'Inter',sans-serif; font-size:12px;
    font-weight:600; color:#1E88E5; background:rgba(30,136,229,.08);
    padding:5px 14px; border-radius:20px; margin-bottom:10px;
}
.contact-heading {
    font-family:'Poppins',sans-serif; font-size:30px; font-weight:800;
    color:#111827; margin:0 0 6px 0;
}
.contact-sub {
    font-family:'Inter',sans-serif; font-size:13px; color:#6B7280; margin:0;
}

.contact-info-card {
    background:linear-gradient(160deg,#14213D 0%,#0D1B2A 100%);
    border-radius:18px; padding:28px; min-height:380px;
}
.ci-title { font-family:'Poppins',sans-serif; font-size:17px; font-weight:600; color:#FFFFFF; margin:0 0 4px 0; }
.ci-subtitle { font-family:'Inter',sans-serif; font-size:12px; color:#94A3B8; margin:0 0 20px 0; }
.ci-row { display:flex; align-items:flex-start; gap:12px; margin-bottom:16px; }
.ci-icon-wrap {
    width:36px; height:36px; border-radius:10px; background:rgba(255,255,255,.06);
    display:flex; align-items:center; justify-content:center; flex-shrink:0;
}
.ci-icon { font-size:16px; }
.ci-label { font-family:'Inter',sans-serif; font-size:10px; color:#94A3B8; font-weight:500; text-transform:uppercase; letter-spacing:.5px; }
.ci-value { font-family:'Inter',sans-serif; font-size:12px; color:#FFFFFF; font-weight:500; margin-top:2px; }

[data-testid="stForm"] {
    background: #FFFFFF !important;
    border: 1px solid #E5E7EB !important;
    border-radius: 18px !important;
    padding: 24px !important;
    box-shadow: 0 4px 16px rgba(0,0,0,.04) !important;
}
</style>"""
