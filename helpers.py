"""
Utility helpers — custom CSS, theming, and shared UI components
"""

import streamlit as st
import re


def apply_custom_css():
    st.markdown("""
    <style>
    /* ── Google Fonts ── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

    /* ── Root & Reset ── */
    :root {
        --primary: #7C3AED;
        --primary-light: #8B5CF6;
        --secondary: #3B82F6;
        --accent: #06B6D4;
        --success: #10B981;
        --warning: #F59E0B;
        --danger: #EF4444;
        --bg-dark: #0F0F1A;
        --bg-card: rgba(255,255,255,0.05);
        --border: rgba(255,255,255,0.1);
        --text-primary: #F1F5F9;
        --text-secondary: #94A3B8;
        --gradient: linear-gradient(135deg, #7C3AED 0%, #3B82F6 100%);
    }

    /* ── App Background ── */
    .stApp {
        background: linear-gradient(135deg, #0F0F1A 0%, #1A1A2E 50%, #16213E 100%) !important;
        font-family: 'Inter', sans-serif !important;
        color: var(--text-primary) !important;
    }

    /* ── Hide default streamlit elements ── */
    #MainMenu, footer, header { visibility: hidden !important; }
    .stDeployButton { display: none !important; }

    /* ── Sidebar ── */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1A0A3B 0%, #0D1B4A 100%) !important;
        border-right: 1px solid var(--border) !important;
    }
    section[data-testid="stSidebar"] .stButton button {
        background: transparent !important;
        border: 1px solid transparent !important;
        color: var(--text-secondary) !important;
        text-align: left !important;
        border-radius: 10px !important;
        margin-bottom: 2px !important;
        transition: all 0.2s ease !important;
        font-size: 14px !important;
    }
    section[data-testid="stSidebar"] .stButton button:hover {
        background: rgba(124, 58, 237, 0.2) !important;
        border-color: var(--primary-light) !important;
        color: #fff !important;
    }
    section[data-testid="stSidebar"] .stButton button[kind="primary"] {
        background: linear-gradient(135deg, #7C3AED, #3B82F6) !important;
        color: #fff !important;
        border: none !important;
    }

    /* ── Sidebar header ── */
    .sidebar-header {
        display: flex; align-items: center; gap: 12px;
        padding: 8px 0 16px;
    }
    .sidebar-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 18px; font-weight: 700;
        background: linear-gradient(135deg, #A78BFA, #60A5FA);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .sidebar-user { font-size: 12px; color: var(--text-secondary); }

    /* ── Auth card ── */
    .auth-card {
        background: rgba(255,255,255,0.03);
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 32px;
        margin: 20px 0;
        backdrop-filter: blur(20px);
    }
    .logo-area { text-align: center; margin-bottom: 24px; }
    .logo-icon { font-size: 48px; }
    .logo-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 28px; font-weight: 700;
        background: linear-gradient(135deg, #A78BFA, #60A5FA);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin: 8px 0 4px;
    }
    .logo-sub { color: var(--text-secondary); font-size: 14px; }

    /* ── Glass cards ── */
    .glass-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 16px;
        padding: 24px;
        backdrop-filter: blur(20px);
        transition: all 0.3s ease;
        margin-bottom: 16px;
    }
    .glass-card:hover {
        border-color: rgba(124,58,237,0.4);
        background: rgba(255,255,255,0.07);
        transform: translateY(-2px);
    }

    /* ── Metric cards ── */
    .metric-card {
        background: linear-gradient(135deg, rgba(124,58,237,0.15), rgba(59,130,246,0.15));
        border: 1px solid rgba(124,58,237,0.3);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
    }
    .metric-value {
        font-size: 36px; font-weight: 700;
        background: linear-gradient(135deg, #A78BFA, #60A5FA);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
    }
    .metric-label { font-size: 13px; color: var(--text-secondary); margin-top: 4px; }

    /* ── Page header ── */
    .page-header {
        background: linear-gradient(135deg, rgba(124,58,237,0.2), rgba(59,130,246,0.2));
        border: 1px solid rgba(124,58,237,0.3);
        border-radius: 16px;
        padding: 24px 28px;
        margin-bottom: 24px;
    }
    .page-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 26px; font-weight: 700; color: #fff;
    }
    .page-sub { color: var(--text-secondary); font-size: 15px; margin-top: 4px; }

    /* ── Tags / Badges ── */
    .skill-tag {
        display: inline-block;
        background: rgba(124,58,237,0.25);
        border: 1px solid rgba(124,58,237,0.5);
        color: #C4B5FD;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        margin: 3px;
    }
    .missing-tag {
        background: rgba(239,68,68,0.15);
        border-color: rgba(239,68,68,0.4);
        color: #FCA5A5;
    }
    .success-tag {
        background: rgba(16,185,129,0.15);
        border-color: rgba(16,185,129,0.4);
        color: #6EE7B7;
    }
    .warning-tag {
        background: rgba(245,158,11,0.15);
        border-color: rgba(245,158,11,0.4);
        color: #FCD34D;
    }

    /* ── Section headings ── */
    .section-title {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 18px; font-weight: 600; color: #E2E8F0;
        margin-bottom: 12px; padding-bottom: 8px;
        border-bottom: 1px solid var(--border);
    }

    /* ── Score circle ── */
    .score-circle {
        width: 120px; height: 120px; border-radius: 50%;
        background: conic-gradient(#7C3AED calc(var(--pct) * 1%), #1E293B 0);
        display: flex; align-items: center; justify-content: center;
        margin: 0 auto;
    }
    .score-inner {
        width: 90px; height: 90px; border-radius: 50%;
        background: #1A1A2E;
        display: flex; align-items: center; justify-content: center;
        font-size: 22px; font-weight: 700; color: #A78BFA;
    }

    /* ── Chat bubbles ── */
    .chat-user {
        background: linear-gradient(135deg, #7C3AED, #3B82F6);
        padding: 12px 16px; border-radius: 16px 16px 4px 16px;
        margin: 8px 0; max-width: 80%; margin-left: auto;
        font-size: 14px; color: #fff;
    }
    .chat-ai {
        background: rgba(255,255,255,0.06);
        border: 1px solid var(--border);
        padding: 12px 16px; border-radius: 16px 16px 16px 4px;
        margin: 8px 0; max-width: 80%;
        font-size: 14px; color: var(--text-primary);
    }

    /* ── Progress bar override ── */
    .stProgress > div > div {
        background: linear-gradient(135deg, #7C3AED, #3B82F6) !important;
        border-radius: 10px !important;
    }

    /* ── Inputs override ── */
    .stTextInput input, .stTextArea textarea, .stSelectbox select {
        background: rgba(255,255,255,0.05) !important;
        border: 1px solid var(--border) !important;
        color: var(--text-primary) !important;
        border-radius: 10px !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: var(--primary-light) !important;
        box-shadow: 0 0 0 2px rgba(124,58,237,0.2) !important;
    }

    /* ── Primary buttons ── */
    .stButton button[kind="primary"] {
        background: linear-gradient(135deg, #7C3AED, #3B82F6) !important;
        border: none !important; color: #fff !important;
        border-radius: 10px !important; font-weight: 600 !important;
        transition: all 0.2s ease !important;
    }
    .stButton button[kind="primary"]:hover {
        opacity: 0.9 !important; transform: translateY(-1px) !important;
    }

    /* ── API status dot ── */
    .api-status { display: flex; align-items: center; gap: 8px; padding: 8px 0; }
    .status-dot {
        width: 8px; height: 8px; border-radius: 50%;
        background: #10B981;
        box-shadow: 0 0 8px #10B981;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }

    /* ── Divider ── */
    hr { border-color: var(--border) !important; }

    /* ── Tabs ── */
    .stTabs [data-baseweb="tab-list"] {
        background: rgba(255,255,255,0.03) !important;
        border-radius: 10px !important;
        padding: 4px !important;
    }
    .stTabs [data-baseweb="tab"] {
        color: var(--text-secondary) !important;
        border-radius: 8px !important;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #7C3AED, #3B82F6) !important;
        color: #fff !important;
    }

    /* ── Expander ── */
    .streamlit-expanderHeader {
        background: rgba(255,255,255,0.04) !important;
        border-radius: 10px !important;
        color: var(--text-primary) !important;
    }
    </style>
    """, unsafe_allow_html=True)


def page_header(icon: str, title: str, subtitle: str = ""):
    st.markdown(f"""
    <div class="page-header">
        <div class="page-title">{icon} {title}</div>
        {f'<div class="page-sub">{subtitle}</div>' if subtitle else ''}
    </div>
    """, unsafe_allow_html=True)


def metric_card(value, label: str, delta: str = ""):
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
        {f'<div style="font-size:12px; color:#10B981; margin-top:4px">{delta}</div>' if delta else ''}
    </div>
    """, unsafe_allow_html=True)


def skill_tags(skills: list, tag_type: str = "default"):
    tag_class = {"default": "skill-tag", "missing": "skill-tag missing-tag",
                 "success": "skill-tag success-tag", "warning": "skill-tag warning-tag"}.get(tag_type, "skill-tag")
    tags_html = "".join(f'<span class="{tag_class}">{s}</span>' for s in skills)
    st.markdown(f'<div>{tags_html}</div>', unsafe_allow_html=True)


def section_title(title: str):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)


def glass_card(content_html: str):
    st.markdown(f'<div class="glass-card">{content_html}</div>', unsafe_allow_html=True)
