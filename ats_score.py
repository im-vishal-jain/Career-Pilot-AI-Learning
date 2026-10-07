"""
ATS Score — detailed ATS compatibility analysis with actionable fixes
"""

import streamlit as st
import json, re
import plotly.graph_objects as go
from utils.helpers import page_header, section_title, skill_tags
from utils.groq_client import quick_analysis
from utils.prompts import ATS_DETAILED_PROMPT

PLOTLY_LAYOUT = dict(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                     font=dict(color="#94A3B8"), margin=dict(l=10, r=10, t=30, b=10))


def _parse(text: str) -> dict:
    text = re.sub(r"```(?:json)?", "", text).strip().rstrip("`").strip()
    try:
        return json.loads(text)
    except Exception:
        m = re.search(r"\{[\s\S]+\}", text)
        return json.loads(m.group()) if m else {}


def _gauge(value: int, title: str, color: str = "#7C3AED") -> go.Figure:
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        title={"text": title, "font": {"color": "#94A3B8", "size": 13}},
        gauge=dict(
            axis=dict(range=[0, 100], tickcolor="#475569"),
            bar=dict(color=color),
            bgcolor="rgba(30,41,59,0.5)",
            steps=[
                dict(range=[0, 50], color="rgba(239,68,68,0.08)"),
                dict(range=[50, 75], color="rgba(245,158,11,0.08)"),
                dict(range=[75, 100], color="rgba(16,185,129,0.08)"),
            ],
        ),
        number=dict(suffix="/100", font=dict(color=color, size=24)),
    ))
    fig.update_layout(height=200, **PLOTLY_LAYOUT)
    return fig


def show():
    page_header("📊", "ATS Score", "Understand exactly how ATS systems read your resume")

    resume_text = st.session_state.get("resume_text", "")
    if not resume_text:
        st.warning("⚠️ Upload your resume first in **Resume Analyzer**.")
        return

    col1, col2 = st.columns([1, 3])
    with col1:
        if st.button("🔍 Run ATS Analysis", type="primary", use_container_width=True):
            with st.spinner("Scanning with ATS engine…"):
                prompt = ATS_DETAILED_PROMPT.format(resume_text=resume_text[:4000])
                raw = quick_analysis(prompt, temperature=0.3, max_tokens=1500)
                st.session_state["ats_detailed"] = _parse(raw)
            st.rerun()

    data = st.session_state.get("ats_detailed")
    if not data:
        st.markdown("""
        <div class="glass-card" style="text-align:center; padding:60px; color:#64748b;">
            <div style="font-size:56px;">📊</div>
            <p style="margin-top:16px;">Click <b>Run ATS Analysis</b> to scan your resume</p>
        </div>""", unsafe_allow_html=True)
        return

    overall = data.get("overall_score", 0)
    color = "#10B981" if overall >= 75 else "#F59E0B" if overall >= 50 else "#EF4444"

    # ── Overall score banner ─────────────────────────────────────────────────
    st.markdown(f"""
    <div class="glass-card" style="display:flex; align-items:center; gap:24px; padding:20px 28px;">
        <div style="font-size:64px; font-weight:800; color:{color}; line-height:1;">{overall}</div>
        <div>
            <div style="color:#E2E8F0; font-size:20px; font-weight:600;">Overall ATS Score</div>
            <div style="color:#64748b; font-size:14px; margin-top:4px;">
                {'Excellent — most ATS systems will pass this resume ✅' if overall >= 75
                 else 'Good — some improvements needed ⚠️' if overall >= 50
                 else 'Needs significant improvement ❌'}
            </div>
        </div>
    </div>""", unsafe_allow_html=True)

    # ── Sub-score gauges ─────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    section_title("📊 Score Breakdown")
    g1, g2, g3 = st.columns(3)
    with g1:
        st.plotly_chart(_gauge(data.get("keyword_score", 0), "Keyword Score", "#7C3AED"),
                        use_container_width=True)
    with g2:
        st.plotly_chart(_gauge(data.get("format_score", 0), "Format Score", "#3B82F6"),
                        use_container_width=True)
    with g3:
        st.plotly_chart(_gauge(data.get("readability_score", 0), "Readability Score", "#06B6D4"),
                        use_container_width=True)

    # ── Section scores ───────────────────────────────────────────────────────
    sec_scores = data.get("section_scores", {})
    if sec_scores:
        section_title("📋 Section Scores")
        for sec, score in sec_scores.items():
            c1, c2, c3 = st.columns([2, 4, 1])
            with c1:
                st.markdown(f'<div style="color:#94A3B8; font-size:13px; padding-top:8px;">{sec.replace("_"," ").title()}</div>',
                            unsafe_allow_html=True)
            with c2:
                st.progress((score or 0) / 100)
            with c3:
                s_color = "#10B981" if score >= 75 else "#F59E0B" if score >= 50 else "#EF4444"
                st.markdown(f'<div style="color:{s_color}; font-weight:600; padding-top:6px;">{score}</div>',
                            unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    tab1, tab2, tab3 = st.tabs(["🔑 Keywords", "⚠️ Issues", "⚡ Quick Wins"])

    with tab1:
        kc1, kc2 = st.columns(2)
        with kc1:
            section_title("✅ Keywords Found")
            skill_tags(data.get("keywords_found", []) or ["None detected"], "success")
        with kc2:
            section_title("❌ Keywords Missing")
            skill_tags(data.get("keywords_missing", []) or ["None"], "missing")

    with tab2:
        issues = data.get("format_issues", [])
        if issues:
            for issue in issues:
                st.markdown(f"""
                <div class="glass-card" style="padding:10px 16px; border-left:3px solid #EF4444;">
                    <span style="color:#FCA5A5; font-size:14px;">⚠️ {issue}</span>
                </div>""", unsafe_allow_html=True)
        else:
            st.success("No major format issues detected!")

    with tab3:
        wins = data.get("quick_wins", [])
        for i, win in enumerate(wins or ["No quick wins listed"], 1):
            st.markdown(f"""
            <div class="glass-card" style="padding:10px 16px; border-left:3px solid #10B981;">
                <span style="color:#6EE7B7; font-weight:600; margin-right:8px;">{i}.</span>
                <span style="color:#E2E8F0; font-size:14px;">{win}</span>
            </div>""", unsafe_allow_html=True)
