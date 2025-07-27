# app.py

import streamlit as st
import os
from utils.pdf_utils import extract_text_from_pdf
from utils.ranker import rank_resumes

st.set_page_config(page_title="Resume Ranker", layout="wide")

st.title("📄 Resume Ranker using Azure OpenAI + LangChain")
st.markdown("Upload a Job Description and up to 10 Resumes (PDF) to see how well each resume matches the JD.")

# Upload Job Description
jd_file = st.file_uploader("📌 Upload Job Description (PDF)", type=["pdf"])

# Upload Resumes
resume_files = st.file_uploader("📥 Upload up to 10 Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

# Submit Button
if st.button("🚀 Rank Resumes"):
    if not jd_file:
        st.error("Please upload a Job Description PDF.")
    elif not resume_files:
        st.error("Please upload at least one resume.")
    elif len(resume_files) > 10:
        st.error("Please upload no more than 10 resumes.")
    else:
        with st.spinner("🔍 Extracting content and ranking resumes..."):

            # Extract JD text
            jd_text = extract_text_from_pdf(jd_file)

            # Extract resumes
            resume_texts = {}
            for resume in resume_files:
                text = extract_text_from_pdf(resume)
                resume_texts[resume.name] = text

            # Rank resumes
            results = rank_resumes(jd_text, resume_texts)

        # Show results
        st.success("✅ Ranking completed!")
        st.subheader("📊 Ranked Resumes")

        for i, res in enumerate(results, start=1):
            st.markdown(f"""
            ### {i}. {res['filename']}
            - **Score:** {res['score']} / 100
            - **Summary:** {res['summary']}
            """)
