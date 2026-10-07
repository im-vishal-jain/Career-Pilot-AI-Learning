"""
Cover Letter Generator — AI-crafted, ATS-friendly cover letters with PDF export
"""

import streamlit as st
import io
from utils.helpers import page_header, section_title
from utils.groq_client import quick_analysis
from utils.prompts import COVER_LETTER_PROMPT


def _export_pdf(text: str, company: str, role: str) -> bytes:
    """Generate a PDF from the cover letter text using ReportLab."""
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import cm
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.colors import HexColor

        buf = io.BytesIO()
        doc = SimpleDocTemplate(buf, pagesize=A4,
                                leftMargin=2.5*cm, rightMargin=2.5*cm,
                                topMargin=2.5*cm, bottomMargin=2.5*cm)
        styles = getSampleStyleSheet()

        title_style = ParagraphStyle(
            "title", parent=styles["Heading1"], fontSize=18, spaceAfter=6,
            textColor=HexColor("#7C3AED"),
        )
        sub_style = ParagraphStyle(
            "sub", parent=styles["Normal"], fontSize=11, spaceAfter=20,
            textColor=HexColor("#64748B"),
        )
        body_style = ParagraphStyle(
            "body", parent=styles["Normal"], fontSize=11, leading=18,
            spaceAfter=12, textColor=HexColor("#1E293B"),
        )

        story = [
            Paragraph(f"Cover Letter — {role}", title_style),
            Paragraph(f"Application to {company}", sub_style),
        ]
        for para in text.split("\n\n"):
            if para.strip():
                story.append(Paragraph(para.strip(), body_style))
                story.append(Spacer(1, 6))

        doc.build(story)
        return buf.getvalue()
    except ImportError:
        return b""


def show():
    page_header("✉️", "Cover Letter Generator", "Create a personalized, ATS-friendly cover letter in seconds")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        section_title("📝 Job Details")
        company = st.text_input("Company Name", placeholder="e.g. Google")
        role = st.text_input("Role / Position", placeholder="e.g. Senior Data Scientist")
        tone = st.selectbox("Tone", ["Professional", "Enthusiastic", "Confident", "Formal"])

        resume_available = bool(st.session_state.get("resume_text"))
        if resume_available:
            st.info("📄 Using your uploaded resume")
            resume_context = st.session_state["resume_text"][:2000]
        else:
            resume_context = st.text_area(
                "Your Background / Skills",
                placeholder="Paste a brief background or key skills…",
                height=120,
            )

        gen_btn = st.button("✨ Generate Cover Letter", type="primary",
                            use_container_width=True,
                            disabled=not (company and role))
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        if gen_btn:
            with st.spinner("✍️ Writing your cover letter…"):
                prompt = COVER_LETTER_PROMPT.format(
                    resume_text=resume_context,
                    company=company,
                    role=role,
                    tone=tone,
                )
                letter = quick_analysis(prompt, temperature=0.75, max_tokens=1200)
                st.session_state["cover_letter"] = letter
                st.session_state["cl_company"] = company
                st.session_state["cl_role"] = role

        letter = st.session_state.get("cover_letter")
        if not letter:
            st.markdown("""
            <div class="glass-card" style="text-align:center; padding:60px; color:#64748b;">
                <div style="font-size:48px;">✉️</div>
                <p style="margin-top:12px;">Fill in the details and generate your cover letter</p>
            </div>""", unsafe_allow_html=True)
            return

        # Display letter
        st.markdown(f"""
        <div class="glass-card" style="border-left:3px solid #7C3AED;">
            <div style="color:#A78BFA; font-weight:600; margin-bottom:12px;">
                ✉️ Cover Letter — {st.session_state.get('cl_role','')} @ {st.session_state.get('cl_company','')}
            </div>
            <div style="color:#E2E8F0; font-size:14px; line-height:1.8; white-space:pre-line;">{letter}</div>
        </div>""", unsafe_allow_html=True)

        # Export options
        st.markdown("<br>", unsafe_allow_html=True)
        ec1, ec2 = st.columns(2)
        with ec1:
            st.download_button(
                "⬇️ Download as Text",
                letter,
                file_name=f"cover_letter_{(st.session_state.get('cl_company','') or 'company').lower().replace(' ','_')}.txt",
                mime="text/plain",
                use_container_width=True,
            )
        with ec2:
            pdf_bytes = _export_pdf(
                letter,
                st.session_state.get("cl_company", "Company"),
                st.session_state.get("cl_role", "Role"),
            )
            if pdf_bytes:
                st.download_button(
                    "📄 Download as PDF",
                    pdf_bytes,
                    file_name="cover_letter.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )
            else:
                st.caption("Install `reportlab` for PDF export")

        # Regenerate / edit
        st.markdown("<br>", unsafe_allow_html=True)
        edited = st.text_area("✏️ Edit Cover Letter", value=letter, height=200)
        if st.button("💾 Save Edits"):
            st.session_state["cover_letter"] = edited
            st.success("Saved!")
