"""
Interview Coach — generate questions, mock interview mode, and answer evaluation
"""

import streamlit as st
import json, re
from utils.helpers import page_header, section_title
from utils.groq_client import quick_analysis
from utils.prompts import INTERVIEW_QUESTIONS_PROMPT, ANSWER_EVALUATION_PROMPT
from utils.database import save_interview_log

ROLES = [
    "Data Scientist", "AI Engineer", "ML Engineer", "Software Engineer",
    "Data Analyst", "Full Stack Developer", "Backend Developer",
    "DevOps Engineer", "Product Manager", "Cybersecurity Analyst",
]

DIFFICULTY_COLORS = {"Easy": "#10B981", "Medium": "#F59E0B", "Hard": "#EF4444"}
TYPE_COLORS = {"Technical": "#7C3AED", "Behavioral": "#3B82F6",
               "HR": "#06B6D4", "Scenario": "#F59E0B"}


def _parse_list(text: str) -> list:
    text = re.sub(r"```(?:json)?", "", text).strip().rstrip("`").strip()
    try:
        return json.loads(text)
    except Exception:
        m = re.search(r"\[[\s\S]+\]", text)
        return json.loads(m.group()) if m else []


def _parse_dict(text: str) -> dict:
    text = re.sub(r"```(?:json)?", "", text).strip().rstrip("`").strip()
    try:
        return json.loads(text)
    except Exception:
        m = re.search(r"\{[\s\S]+\}", text)
        return json.loads(m.group()) if m else {}


def show():
    page_header("🎤", "Interview Coach", "Practice with AI-generated questions and get real-time feedback")

    mode = st.radio("Mode", ["📋 Question Bank", "🎯 Mock Interview"], horizontal=True)
    st.markdown("---")

    if mode == "📋 Question Bank":
        _question_bank_mode()
    else:
        _mock_interview_mode()


def _question_bank_mode():
    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        section_title("⚙️ Settings")
        role = st.selectbox("Role", ROLES)
        q_count = st.slider("Number of questions", 5, 20, 10)
        q_types = st.multiselect(
            "Question types",
            ["Technical", "Behavioral", "HR", "Scenario"],
            default=["Technical", "Behavioral"],
        )
        gen_btn = st.button("⚡ Generate Questions", type="primary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        if gen_btn:
            type_str = ", ".join(q_types) if q_types else "all types"
            prompt = INTERVIEW_QUESTIONS_PROMPT.format(role=role, count=q_count) + \
                     f"\nFocus on these types: {type_str}"
            with st.spinner("🤖 Generating interview questions…"):
                raw = quick_analysis(prompt, temperature=0.7, max_tokens=2000)
                questions = _parse_list(raw)
                st.session_state["interview_questions"] = questions
                st.session_state["interview_role"] = role

        questions = st.session_state.get("interview_questions", [])
        if not questions:
            st.markdown("""
            <div class="glass-card" style="text-align:center; padding:60px; color:#64748b;">
                <div style="font-size:48px">🎤</div>
                <p style="margin-top:12px;">Generate questions to start preparing</p>
            </div>""", unsafe_allow_html=True)
            return

        for i, q in enumerate(questions, 1):
            d_color = DIFFICULTY_COLORS.get(q.get("difficulty", ""), "#94A3B8")
            t_color = TYPE_COLORS.get(q.get("type", ""), "#94A3B8")

            with st.expander(f"**Q{i}.** {q.get('question', '')[:80]}…"):
                badges = f"""
                <span style="background:rgba(124,58,237,0.2); color:{t_color}; font-size:11px; padding:3px 10px; border-radius:10px; margin-right:6px;">{q.get('type','')}</span>
                <span style="background:rgba(239,68,68,0.1); color:{d_color}; font-size:11px; padding:3px 10px; border-radius:10px;">{q.get('difficulty','')}</span>
                """
                st.markdown(badges, unsafe_allow_html=True)
                st.markdown(f"**Question:** {q.get('question','')}")
                st.markdown("---")
                st.markdown("**💡 Ideal Answer:**")
                st.markdown(f">{q.get('ideal_answer','')}")
                if q.get("tips"):
                    st.info(f"**Tips:** {q.get('tips')}")


def _mock_interview_mode():
    role = st.selectbox("Target Role", ROLES, key="mock_role")

    if "mock_questions" not in st.session_state or st.session_state.get("mock_role_used") != role:
        if st.button("🚀 Start Mock Interview", type="primary"):
            with st.spinner("Preparing your interview…"):
                prompt = INTERVIEW_QUESTIONS_PROMPT.format(role=role, count=8)
                raw = quick_analysis(prompt, temperature=0.7, max_tokens=2000)
                qs = _parse_list(raw)
                st.session_state["mock_questions"] = qs
                st.session_state["mock_current"] = 0
                st.session_state["mock_answers"] = []
                st.session_state["mock_scores"] = []
                st.session_state["mock_role_used"] = role
            st.rerun()
        return

    questions = st.session_state.get("mock_questions", [])
    current = st.session_state.get("mock_current", 0)
    scores = st.session_state.get("mock_scores", [])

    if current >= len(questions):
        # ── Results ──────────────────────────────────────────────────────
        avg = round(sum(scores) / len(scores), 1) if scores else 0
        color = "#10B981" if avg >= 7 else "#F59E0B" if avg >= 5 else "#EF4444"
        st.markdown(f"""
        <div class="glass-card" style="text-align:center; padding:32px;">
            <div style="font-size:56px; color:{color}; font-weight:800;">{avg}/10</div>
            <div style="color:#E2E8F0; font-size:20px; margin-top:8px;">Interview Complete!</div>
            <div style="color:#64748b; font-size:14px; margin-top:4px;">
                {'Great job! 🎉' if avg >= 7 else 'Keep practicing! 💪' if avg >= 5 else 'Study more and retry!'}
            </div>
        </div>""", unsafe_allow_html=True)

        save_interview_log(st.session_state.get("user_id", 1), role, int(avg * 10), len(questions))

        if st.button("🔄 Restart Interview", type="primary"):
            for k in ["mock_questions", "mock_current", "mock_answers", "mock_scores", "mock_role_used"]:
                st.session_state.pop(k, None)
            st.rerun()
        return

    # ── Current question ─────────────────────────────────────────────────────
    q = questions[current]
    progress = (current) / len(questions)
    st.progress(progress)
    st.caption(f"Question {current + 1} of {len(questions)}")

    d_color = DIFFICULTY_COLORS.get(q.get("difficulty", ""), "#94A3B8")
    t_color = TYPE_COLORS.get(q.get("type", ""), "#94A3B8")

    st.markdown(f"""
    <div class="glass-card" style="border-left:3px solid #7C3AED;">
        <div style="margin-bottom:10px;">
            <span style="color:{t_color}; font-size:12px; font-weight:600;">{q.get('type','')}</span>
            <span style="color:{d_color}; font-size:12px; margin-left:12px;">{q.get('difficulty','')}</span>
        </div>
        <div style="color:#E2E8F0; font-size:16px; font-weight:500; line-height:1.6;">{q.get('question','')}</div>
    </div>""", unsafe_allow_html=True)

    answer = st.text_area("Your Answer", height=150, key=f"mock_ans_{current}",
                          placeholder="Type your answer here…")

    if st.button("Submit Answer →", type="primary", disabled=not answer.strip()):
        with st.spinner("Evaluating your answer…"):
            eval_prompt = ANSWER_EVALUATION_PROMPT.format(
                role=role, question=q.get("question", ""), answer=answer
            )
            raw = quick_analysis(eval_prompt, temperature=0.4, max_tokens=800)
            eval_data = _parse_dict(raw)
            score = eval_data.get("score", 5)

        st.session_state["mock_answers"].append(answer)
        st.session_state["mock_scores"].append(score)

        score_color = "#10B981" if score >= 7 else "#F59E0B" if score >= 5 else "#EF4444"
        st.markdown(f"""
        <div class="glass-card">
            <div style="font-size:28px; font-weight:700; color:{score_color};">{score}/10</div>
            <p style="color:#E2E8F0; margin-top:8px;">{eval_data.get('feedback','')}</p>
            <div style="margin-top:12px; color:#6EE7B7; font-size:13px;">
                {''.join(f'✓ {s}<br>' for s in eval_data.get('strengths',[]))}
            </div>
            <div style="margin-top:8px; color:#FCA5A5; font-size:13px;">
                {''.join(f'✗ {i}<br>' for i in eval_data.get('improvements',[]))}
            </div>
        </div>""", unsafe_allow_html=True)

        if st.button("Next Question →", type="primary"):
            st.session_state["mock_current"] = current + 1
            st.rerun()
