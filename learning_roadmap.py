"""
Learning Roadmap — AI-generated 30/90/180-day career learning plans
"""

import streamlit as st
from utils.helpers import page_header, section_title
from utils.groq_client import stream_chat
from utils.prompts import ROADMAP_PROMPT

ROLES = [
    "Data Scientist", "AI Engineer", "ML Engineer", "Software Engineer",
    "Data Analyst", "Full Stack Developer", "Backend Developer",
    "DevOps Engineer", "Cybersecurity Analyst", "Product Manager",
]

DURATIONS = {
    "30 Days": ("30 days", "Week 1–2", "Week 3", "Week 4", "30 Days"),
    "90 Days": ("90 days", "Month 1", "Month 2", "Month 3", "90 Days"),
    "6 Months": ("6 months", "Months 1–2", "Months 3–4", "Months 5–6", "6 Months"),
}


def show():
    page_header("📚", "Learning Roadmap", "Get a personalized step-by-step learning plan powered by AI")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        section_title("⚙️ Configure Roadmap")
        role = st.selectbox("Target Role", ROLES)
        custom = st.text_input("Custom role", placeholder="Optional override…")
        if custom.strip():
            role = custom.strip()

        duration_key = st.radio("Duration", list(DURATIONS.keys()), horizontal=True)
        duration, p1, p2, p3, dur_label = DURATIONS[duration_key]

        background = st.text_area(
            "Your Background (optional)",
            placeholder="e.g. 2 years Python experience, know basic ML, familiar with SQL…",
            height=100,
        )
        if not background.strip() and st.session_state.get("resume_text"):
            background = st.session_state["resume_text"][:800]
            st.caption("Using your uploaded resume as background context")

        gen_btn = st.button("🗺️ Generate Roadmap", type="primary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        if gen_btn:
            st.session_state["roadmap_content"] = ""
            prompt = ROADMAP_PROMPT.format(
                role=role,
                background=background or "General beginner",
                duration=duration,
                phase1=p1, phase2=p2, phase3=p3,
            )
            st.markdown(f"""
            <div class="glass-card" style="border-left:3px solid #7C3AED; margin-bottom:16px;">
                <div style="color:#A78BFA; font-weight:600;">🗺️ {dur_label} Roadmap — {role}</div>
            </div>""", unsafe_allow_html=True)

            messages = [{"role": "user", "content": prompt}]
            with st.container():
                content_placeholder = st.empty()
                full = ""
                for chunk in stream_chat(messages, max_tokens=2500, temperature=0.6):
                    full += chunk
                    content_placeholder.markdown(full)
                st.session_state["roadmap_content"] = full

            st.success("✅ Roadmap generated!")

            if st.session_state.get("roadmap_content"):
                st.download_button(
                    "⬇️ Download Roadmap (.md)",
                    st.session_state["roadmap_content"],
                    file_name=f"roadmap_{role.lower().replace(' ','_')}_{duration_key.replace(' ','')}.md",
                    mime="text/markdown",
                )

        elif st.session_state.get("roadmap_content"):
            st.markdown(st.session_state["roadmap_content"])
            if st.download_button(
                "⬇️ Download Roadmap (.md)",
                st.session_state["roadmap_content"],
                file_name="roadmap.md",
                mime="text/markdown",
            ):
                pass
        else:
            st.markdown("""
            <div class="glass-card" style="text-align:center; padding:60px; color:#64748b;">
                <div style="font-size:56px;">📚</div>
                <p style="margin-top:16px; font-size:15px;">Configure your roadmap and click Generate</p>
                <p style="font-size:13px; margin-top:8px;">Personalized learning paths for 30 days to 6 months</p>
            </div>""", unsafe_allow_html=True)
