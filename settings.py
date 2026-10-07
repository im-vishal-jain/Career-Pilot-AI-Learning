"""
Settings — API key management, user profile, and app preferences
"""

import streamlit as st
from utils.helpers import page_header, section_title


def show():
    page_header("⚙️", "Settings", "Manage your account, API key, and preferences")

    tab1, tab2, tab3 = st.tabs(["👤 Profile", "🔑 API Key", "🗂️ Data"])

    with tab1:
        section_title("User Profile")
        st.markdown(f"""
        <div class="glass-card">
            <div style="display:flex; align-items:center; gap:16px;">
                <div style="width:56px; height:56px; border-radius:50%; background:linear-gradient(135deg,#7C3AED,#3B82F6);
                    display:flex; align-items:center; justify-content:center;
                    font-size:22px; font-weight:700; color:#fff;">
                    {st.session_state.get('username','U')[0].upper()}
                </div>
                <div>
                    <div style="color:#E2E8F0; font-size:18px; font-weight:600;">{st.session_state.get('username','—')}</div>
                    <div style="color:#64748b; font-size:13px;">Career Copilot User</div>
                </div>
            </div>
        </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        with col1:
            st.metric("ATS Score", f"{st.session_state.get('ats_score', 0)}/100")
            st.metric("Skills Detected", len(st.session_state.get("resume_data", {}).get("skills", [])))
        with col2:
            st.metric("Job Match", f"{st.session_state.get('job_match', {}).get('match_percentage', 0)}%")
            st.metric("Sessions", "Active")

    with tab2:
        section_title("🔑 Groq API Key")
        st.markdown("""
        <div class="glass-card" style="border-left:3px solid #F59E0B;">
            <p style="color:#FCD34D; font-size:13px;">
                Your API key is stored only in your current session and never saved to disk.
                Get a free key at <a href="https://console.groq.com" target="_blank" style="color:#60A5FA;">console.groq.com</a>
            </p>
        </div>""", unsafe_allow_html=True)

        current_key = st.session_state.get("groq_api_key", "")
        masked = f"{current_key[:8]}{'*' * (len(current_key) - 12)}{current_key[-4:]}" if len(current_key) > 16 else "Not set"

        st.markdown(f'<div style="color:#94A3B8; font-size:13px;">Current key: <code>{masked}</code></div>',
                    unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

        new_key = st.text_input("Update API Key", type="password", placeholder="gsk_…")
        if st.button("💾 Save Key", type="primary"):
            if new_key.strip():
                st.session_state["groq_api_key"] = new_key.strip()
                st.success("✅ API key updated!")
            else:
                st.error("Please enter a valid key.")

        st.markdown("<br>", unsafe_allow_html=True)
        section_title("🤖 Model Selection")
        model_options = [
            "llama-3.3-70b-versatile",
            "llama-3.1-8b-instant",
            "mixtral-8x7b-32768",
            "gemma2-9b-it",
            "deepseek-r1-distill-llama-70b",
        ]
        current_model = st.session_state.get("preferred_model", model_options[0])
        selected_model = st.selectbox("Preferred Model", model_options,
                                      index=model_options.index(current_model) if current_model in model_options else 0)
        if st.button("💾 Save Model Preference"):
            st.session_state["preferred_model"] = selected_model
            # Update groq_client default
            import utils.groq_client as gc
            gc.MODEL = selected_model
            st.success(f"Model set to {selected_model}")

    with tab3:
        section_title("🗂️ Session Data")

        data_items = {
            "Resume Text": len(st.session_state.get("resume_text", "")),
            "Resume Analysis": bool(st.session_state.get("resume_data")),
            "Job Match Data": bool(st.session_state.get("job_match")),
            "Skill Gap Data": bool(st.session_state.get("skill_gap_data")),
            "Interview Questions": len(st.session_state.get("interview_questions", [])),
            "Cover Letter": bool(st.session_state.get("cover_letter")),
            "Learning Roadmap": bool(st.session_state.get("roadmap_content")),
        }

        for item, val in data_items.items():
            status = "✅" if val else "❌"
            detail = f"{val} chars" if isinstance(val, int) and val > 0 else ("Loaded" if val is True else "—")
            st.markdown(f"""
            <div class="glass-card" style="padding:10px 16px; display:flex; justify-content:space-between;">
                <span style="color:#E2E8F0; font-size:14px;">{status} {item}</span>
                <span style="color:#64748b; font-size:13px;">{detail}</span>
            </div>""", unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🗑️ Clear All Session Data", type="secondary"):
            keys_to_clear = ["resume_text", "resume_data", "ats_score", "job_match",
                             "skill_gap_data", "interview_questions", "cover_letter",
                             "roadmap_content", "ats_detailed", "mock_questions",
                             "mock_current", "mock_answers", "mock_scores"]
            for k in keys_to_clear:
                st.session_state.pop(k, None)
            st.success("Session data cleared.")
            st.rerun()

        section_title("ℹ️ About")
        st.markdown("""
        <div class="glass-card">
            <div style="color:#A78BFA; font-size:16px; font-weight:600; margin-bottom:8px;">🚀 Career Copilot AI v1.0</div>
            <div style="color:#64748b; font-size:13px; line-height:1.8;">
                Built with Streamlit · Groq API (LLaMA 3.3 70B) · SQLite<br>
                Features: Resume Analysis · Job Matching · Skill Gap · Interview Coach<br>
                Learning Roadmap · Cover Letter · ATS Score · Career Recommendations
            </div>
        </div>""", unsafe_allow_html=True)
