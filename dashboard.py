"""
Dashboard — overview metrics, charts, and quick actions
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from utils.helpers import page_header, metric_card, section_title
from utils.database import get_user_sessions, get_interview_logs

PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="#94A3B8", family="Inter"),
    margin=dict(l=10, r=10, t=30, b=10),
)


def show():
    page_header("🏠", "Dashboard", "Your career progress at a glance")

    user_id = st.session_state.get("user_id", 1)
    sessions = get_user_sessions(user_id)
    interview_logs = get_interview_logs(user_id)

    resume_data = st.session_state.get("resume_data", {})
    ats_score = st.session_state.get("ats_score", 0)
    job_match = st.session_state.get("job_match", {})

    # ── Top metrics ──────────────────────────────────────────────────────────
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        metric_card(f"{ats_score}/100", "ATS Score", "↑ Resume uploaded" if ats_score else "Upload resume")
    with c2:
        match_pct = job_match.get("match_percentage", 0)
        metric_card(f"{match_pct}%", "Job Match", "↑ Run matcher" if match_pct else "Run Job Matcher")
    with c3:
        skill_count = len(resume_data.get("skills", []))
        metric_card(str(skill_count), "Skills Detected", f"{skill_count} skills found" if skill_count else "Analyze resume")
    with c4:
        interview_count = len(interview_logs)
        metric_card(str(interview_count), "Interviews Practiced", f"{interview_count} sessions" if interview_count else "Try Coach")

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Quick actions ────────────────────────────────────────────────────────
    section_title("⚡ Quick Actions")
    qa1, qa2, qa3, qa4 = st.columns(4)
    with qa1:
        if st.button("📄 Analyze Resume", use_container_width=True, type="primary"):
            st.session_state.current_page = "resume_analyzer"; st.rerun()
    with qa2:
        if st.button("🎯 Match Job", use_container_width=True, type="primary"):
            st.session_state.current_page = "job_matcher"; st.rerun()
    with qa3:
        if st.button("🎤 Practice Interview", use_container_width=True, type="primary"):
            st.session_state.current_page = "interview_coach"; st.rerun()
    with qa4:
        if st.button("✉️ Write Cover Letter", use_container_width=True, type="primary"):
            st.session_state.current_page = "cover_letter"; st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    col_left, col_right = st.columns([3, 2])

    with col_left:
        # ── Skills radar chart ────────────────────────────────────────────
        section_title("🕸️ Skills Overview")
        skills = resume_data.get("skills", [])
        if skills and ats_score:
            categories = skills[:8] if len(skills) >= 8 else skills + ["?"] * (8 - len(skills))
            import random; random.seed(42)
            values = [random.randint(50, 95) for _ in categories]
            fig = go.Figure(go.Scatterpolar(
                r=values + [values[0]],
                theta=categories + [categories[0]],
                fill="toself",
                line_color="#7C3AED",
                fillcolor="rgba(124,58,237,0.25)",
                name="Skills",
            ))
            fig.update_layout(
                polar=dict(
                    radialaxis=dict(visible=True, range=[0, 100], color="#475569"),
                    angularaxis=dict(color="#94A3B8"),
                    bgcolor="rgba(0,0,0,0)",
                ),
                showlegend=False,
                height=320,
                **PLOTLY_LAYOUT,
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.markdown("""
            <div class="glass-card" style="text-align:center; padding:40px; color:#64748b;">
                <div style="font-size:40px">📄</div>
                <p style="margin-top:12px">Upload your resume to see your skills radar chart</p>
            </div>""", unsafe_allow_html=True)

        # ── Interview performance line graph ─────────────────────────────
        if interview_logs:
            section_title("📈 Interview Performance")
            df = pd.DataFrame(interview_logs)
            df["created_at"] = pd.to_datetime(df["created_at"])
            fig2 = px.line(df, x="created_at", y="score", color_discrete_sequence=["#7C3AED"],
                           markers=True, labels={"created_at": "Date", "score": "Score"})
            fig2.update_layout(height=220, **PLOTLY_LAYOUT)
            fig2.update_traces(line_width=2.5, marker_size=7)
            st.plotly_chart(fig2, use_container_width=True)

    with col_right:
        # ── ATS score gauge ──────────────────────────────────────────────
        section_title("🎯 ATS Score")
        if ats_score:
            color = "#10B981" if ats_score >= 75 else "#F59E0B" if ats_score >= 50 else "#EF4444"
            fig3 = go.Figure(go.Indicator(
                mode="gauge+number",
                value=ats_score,
                gauge=dict(
                    axis=dict(range=[0, 100], tickcolor="#475569"),
                    bar=dict(color=color),
                    bgcolor="rgba(30,41,59,0.5)",
                    steps=[
                        dict(range=[0, 50], color="rgba(239,68,68,0.1)"),
                        dict(range=[50, 75], color="rgba(245,158,11,0.1)"),
                        dict(range=[75, 100], color="rgba(16,185,129,0.1)"),
                    ],
                    threshold=dict(line=dict(color="white", width=2), thickness=0.75, value=75),
                ),
                number=dict(suffix="/100", font=dict(color=color, size=32)),
            ))
            fig3.update_layout(height=240, **PLOTLY_LAYOUT)
            st.plotly_chart(fig3, use_container_width=True)
        else:
            st.info("Analyze your resume to see ATS score")

        # ── Skills pie chart ─────────────────────────────────────────────
        if resume_data.get("skills"):
            section_title("📊 Skill Categories")
            cats = {
                "Programming": sum(1 for s in resume_data["skills"] if any(x in s.lower() for x in ["python","java","js","c++","go","rust","sql","r "])),
                "ML/AI": sum(1 for s in resume_data["skills"] if any(x in s.lower() for x in ["ml","ai","deep","nlp","tensorflow","pytorch","sklearn"])),
                "DevOps": sum(1 for s in resume_data["skills"] if any(x in s.lower() for x in ["docker","k8s","aws","gcp","azure","ci","cd","git"])),
                "Other": 0,
            }
            cats["Other"] = max(0, len(resume_data["skills"]) - sum(cats.values()))
            cats = {k: v for k, v in cats.items() if v > 0}
            if cats:
                fig4 = px.pie(values=list(cats.values()), names=list(cats.keys()),
                              color_discrete_sequence=["#7C3AED", "#3B82F6", "#06B6D4", "#10B981"],
                              hole=0.5)
                fig4.update_layout(height=220, showlegend=True, **PLOTLY_LAYOUT)
                fig4.update_traces(textfont_color="white")
                st.plotly_chart(fig4, use_container_width=True)

    # ── Recent sessions ──────────────────────────────────────────────────────
    if sessions:
        section_title("📋 Recent Sessions")
        for s in sessions[:3]:
            st.markdown(f"""
            <div class="glass-card" style="padding:14px 18px; display:flex; justify-content:space-between; align-items:center;">
                <div>
                    <div style="color:#E2E8F0; font-weight:500; font-size:14px;">Resume Analysis</div>
                    <div style="color:#64748b; font-size:12px;">{s['created_at'][:16]}</div>
                </div>
                <div style="font-size:20px; font-weight:700; color:#A78BFA;">{s['ats_score'] or '—'}</div>
            </div>""", unsafe_allow_html=True)
