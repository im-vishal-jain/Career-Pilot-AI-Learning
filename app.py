"""
Career Copilot AI — Main Application Entry Point
Production-ready AI career assistant using Groq API + Streamlit
"""

import streamlit as st
import os
from utils.database import init_db, get_user, create_user, verify_password
from utils.helpers import apply_custom_css

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Career Copilot AI",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_custom_css()
init_db()


# ── Session state defaults ────────────────────────────────────────────────────
def init_session():
    defaults = {
        "authenticated": False,
        "username": None,
        "user_id": None,
        "groq_api_key": "",
        "resume_text": "",
        "resume_data": {},
        "ats_score": None,
        "job_match": {},
        "chat_history": [],
        "theme": "dark",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


init_session()


# ── Auth UI ──────────────────────────────────────────────────────────────────
def login_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div class="auth-card">
            <div class="logo-area">
                <span class="logo-icon">🚀</span>
                <h1 class="logo-title">Career Copilot AI</h1>
                <p class="logo-sub">Your AI-powered career growth partner</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        tab1, tab2 = st.tabs(["🔐 Login", "✨ Sign Up"])

        with tab1:
            with st.form("login_form"):
                username = st.text_input("Username", placeholder="Enter your username")
                password = st.text_input("Password", type="password", placeholder="Enter your password")
                groq_key = st.text_input("Groq API Key", type="password",
                                         placeholder="gsk_...",
                                         help="Get your free API key at console.groq.com")
                submitted = st.form_submit_button("Login →", use_container_width=True)

                if submitted:
                    if not username or not password or not groq_key:
                        st.error("Please fill in all fields.")
                    else:
                        user = get_user(username)
                        if user and verify_password(password, user["password_hash"]):
                            st.session_state.authenticated = True
                            st.session_state.username = username
                            st.session_state.user_id = user["id"]
                            st.session_state.groq_api_key = groq_key
                            st.success("Welcome back! Redirecting…")
                            st.rerun()
                        else:
                            st.error("Invalid username or password.")

        with tab2:
            with st.form("signup_form"):
                new_user = st.text_input("Choose a Username", placeholder="e.g. john_doe")
                new_email = st.text_input("Email", placeholder="you@example.com")
                new_pass = st.text_input("Password", type="password", placeholder="Min 6 characters")
                groq_key2 = st.text_input("Groq API Key", type="password",
                                          placeholder="gsk_...",
                                          help="Get your free key at console.groq.com")
                submitted2 = st.form_submit_button("Create Account →", use_container_width=True)

                if submitted2:
                    if not all([new_user, new_email, new_pass, groq_key2]):
                        st.error("Please fill in all fields.")
                    elif len(new_pass) < 6:
                        st.error("Password must be at least 6 characters.")
                    elif get_user(new_user):
                        st.error("Username already taken.")
                    else:
                        create_user(new_user, new_email, new_pass)
                        st.success("Account created! Please login.")


# ── Sidebar nav ───────────────────────────────────────────────────────────────
def sidebar():
    with st.sidebar:
        st.markdown(f"""
        <div class="sidebar-header">
            <span style="font-size:2rem;">🚀</span>
            <div>
                <div class="sidebar-title">Career Copilot</div>
                <div class="sidebar-user">👤 {st.session_state.username}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        pages = {
            "🏠 Dashboard": "dashboard",
            "📄 Resume Analyzer": "resume_analyzer",
            "🎯 Job Matcher": "job_matcher",
            "🧠 Skill Gap Analysis": "skill_gap",
            "📚 Learning Roadmap": "learning_roadmap",
            "🎤 Interview Coach": "interview_coach",
            "✉️ Cover Letter": "cover_letter",
            "📊 ATS Score": "ats_score",
            "⚙️ Settings": "settings",
        }

        if "current_page" not in st.session_state:
            st.session_state.current_page = "dashboard"

        for label, key in pages.items():
            active = st.session_state.current_page == key
            btn_class = "nav-btn-active" if active else "nav-btn"
            if st.button(label, key=f"nav_{key}",
                         use_container_width=True,
                         type="primary" if active else "secondary"):
                st.session_state.current_page = key
                st.rerun()

        st.markdown("---")
        if st.button("🚪 Logout", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

        # API key status
        st.markdown("""
        <div class="api-status">
            <span class="status-dot"></span>
            <span style="font-size:12px; color:#a0aec0;">Groq API Connected</span>
        </div>
        """, unsafe_allow_html=True)


# ── Page router ───────────────────────────────────────────────────────────────
def route_page():
    page = st.session_state.get("current_page", "dashboard")
    if page == "dashboard":
        from pages.dashboard import show
    elif page == "resume_analyzer":
        from pages.resume_analyzer import show
    elif page == "job_matcher":
        from pages.job_matcher import show
    elif page == "skill_gap":
        from pages.skill_gap import show
    elif page == "learning_roadmap":
        from pages.learning_roadmap import show
    elif page == "interview_coach":
        from pages.interview_coach import show
    elif page == "cover_letter":
        from pages.cover_letter import show
    elif page == "ats_score":
        from pages.ats_score import show
    elif page == "settings":
        from pages.settings import show
    else:
        from pages.dashboard import show
    show()


# ── Main ─────────────────────────────────────────────────────────────────────
if not st.session_state.authenticated:
    login_page()
else:
    sidebar()
    route_page()
