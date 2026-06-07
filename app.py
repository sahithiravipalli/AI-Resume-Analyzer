import streamlit as st

from extractor import (
    extract_text_from_pdf,
    extract_email,
    extract_phone
)

from skills import extract_skills
from ats import calculate_ats_score
from summary import generate_summary
from suggestions import generate_suggestions

from job_match import (
    job_roles,
    calculate_job_match
)

from database import save_analysis

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🚀",
    layout="wide"
)
theme = st.sidebar.selectbox(
    "🎨 Choose Theme",
    ["System", "Light", "Dark"]
)

if theme == "Dark":
    st.markdown("""
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

elif theme == "Light":
    st.markdown("""
    <style>
    .stApp {
        background-color: white;
        color: black;
    }
    </style>
    """, unsafe_allow_html=True)
st.sidebar.title("🚀 AI Resume Analyzer")

st.sidebar.info(
    """
    Upload a resume PDF and get:

    ✅ ATS Score

    ✅ Skill Detection

    ✅ Resume Summary

    ✅ Improvement Suggestions

    ✅ Job Role Match

    ✅ Downloadable Report
    """
)

st.title("🚀 AI Resume Analyzer")

st.markdown(
    """
    Analyze resumes, evaluate ATS scores,
    detect skills, and match candidates
    to job roles.
    """
)

uploaded_file = st.file_uploader(
    "📄 Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file:

    text = extract_text_from_pdf(uploaded_file)

    email = extract_email(text)
    phone = extract_phone(text)

    skills = extract_skills(text)

    summary = generate_summary(skills)

    suggestions = generate_suggestions(
        text,
        skills
    )

    ats_score = calculate_ats_score(
        email,
        phone,
        skills,
        text
    )

    selected_role = st.selectbox(
        "🎯 Select Target Role",
        list(job_roles.keys())
    )

    match_score, matched, missing = (
        calculate_job_match(
            selected_role,
            skills
        )
    )

    save_analysis(
        email,
        phone,
        ats_score,
        selected_role
    )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "📊 ATS Score",
            f"{ats_score}/100"
        )

        st.progress(
            ats_score / 100
        )

    with col2:
        st.metric(
            "🎯 Match Score",
            f"{match_score}%"
        )

        st.progress(
            match_score / 100
        )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📞 Contact Information")

        st.write(
            "📧 Email:",
            email
        )

        st.write(
            "📱 Phone:",
            phone
        )

    with col2:

        st.subheader("🛠 Skills Detected")

        if skills:
            st.success(
                ", ".join(skills)
            )
        else:
            st.warning(
                "No skills detected"
            )

    st.markdown("---")

    st.subheader("📝 Resume Summary")

    st.info(summary)

    st.markdown("---")

    st.subheader(
        "💡 Improvement Suggestions"
    )

    if suggestions:

        for suggestion in suggestions:

            st.warning(
                suggestion
            )

    else:

        st.success(
            "No major improvements needed."
        )

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "✅ Matched Skills"
        )

        if matched:
            st.success(
                ", ".join(matched)
            )
        else:
            st.warning(
                "No matching skills found"
            )

    with col2:

        st.subheader(
            "❌ Missing Skills"
        )

        if missing:
            st.error(
                ", ".join(missing)
            )
        else:
            st.success(
                "All required skills detected"
            )

    report = f"""
AI Resume Analysis Report

ATS Score: {ats_score}/100

Email:
{email}

Phone:
{phone}

Skills:
{', '.join(skills)}

Resume Summary:
{summary}

Improvement Suggestions:
{', '.join(suggestions)}

Target Role:
{selected_role}

Job Match Score:
{match_score}%
"""

    st.markdown("---")

    st.download_button(
        label="📥 Download Report",
        data=report,
        file_name="resume_analysis_report.txt",
        mime="text/plain"
    )

    st.markdown("---")

    with st.expander(
        "📄 View Resume Content"
    ):

        st.text_area(
            "Resume Content",
            text,
            height=350
        )