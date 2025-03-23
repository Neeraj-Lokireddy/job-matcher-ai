import sys
import os
import streamlit as st

# ✅ Fix imports by setting correct path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.resume_parser.parser import parse_resume
from src.job_fetcher.fetcher import fetch_jobs
from src.matcher.matcher import rank_jobs

# 🔑 Replace with your real API key
API_KEY = "05de988aa849220cfd18924d5f1cc19b0b246a3dc53339a1535782ae240d6ceb"

# 🎨 Streamlit config
st.set_page_config(page_title="AI Job Matchmaker", layout="wide")
st.title("🔍 AI-Powered Job Matchmaker")

# File uploader
uploaded_file = st.file_uploader("📄 Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())
    
    st.success("Resume uploaded successfully!")

    # ✅ Parse the resume
    parsed = parse_resume("temp_resume.pdf")

    # 📋 Display parsed resume info
    st.subheader("📋 Resume Summary")
    st.write(f"**Email:** {parsed['email']}")
    st.write(f"**Skills:** {', '.join(parsed['skills'])}")
    st.write(f"**Education:** {', '.join(parsed['education'])}")
    st.write(f"**Experience:** {', '.join(parsed['experience'])}")

    # 📍 Job preferences input
    st.subheader("📍 Job Preferences")
    job_title = st.text_input("Job Title", value="data scientist")
    location = st.text_input("Location", value="Kansas City")

    if st.button("Find Matching Jobs"):
        with st.spinner("Fetching and ranking job listings..."):
            jobs = fetch_jobs(job_title, location, API_KEY, num_results=30)
            matches = rank_jobs(parsed["raw_text"], jobs)
            st.session_state.matches = matches
            st.session_state.job_count = 5  # Reset count

# 🎯 Show top matches
if "matches" in st.session_state:
    st.subheader("🎯 Top Matching Jobs")

    matches = st.session_state.matches
    job_count = st.session_state.job_count

    for i, job in enumerate(matches[:job_count], 1):
        st.markdown(f"### {i}. {job['title']} — {job['company']}")
        st.markdown(f"**Location:** {job['location']}")
        st.markdown(f"**Score:** {job['score']}")
        st.markdown(f"**Description:** {job['description'][:300]}...")

        if job.get("link"):
            st.markdown(f"[📝 Apply Now]({job['link']})", unsafe_allow_html=True)
        else:
            st.info("🔗 No application link available.")

        st.markdown("---")

    # 🔘 Show more button
    if job_count < len(matches):
        if st.button("🔽 Show More Jobs"):
            st.session_state.job_count = min(job_count + 5, len(matches))

