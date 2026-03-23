import streamlit as st
import requests

st.title("📄 AI Resume Screening System")

# upload file
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# job description input
job_description = st.text_area("Enter Job Description")

if st.button("Analyze Resume"):
    if uploaded_file is not None and job_description:

        files = {"file": uploaded_file}
        data = {"job_description": job_description}

        response = requests.post(
            "https://ai-resume-screening-f9wk.onrender.com/predict",
            files=files,
            data=data
        )

        st.write("Status Code:", response.status_code)

        try:
            result = response.json()
            st.write("API Response:", result)  # debug

            st.subheader("📊 Results")

            st.write(f"TF-IDF Score: {result.get('tfidf_score', 'N/A')}%")
            st.write(f"Skill Match Score: {result.get('skill_score', 'N/A')}%")
            st.write(f"Final Score: {result.get('final_score', 'N/A')}%")

            st.subheader("✅ Matched Skills")
            st.write(result.get("matched_skills", []))

            st.subheader("❌ Missing Skills")
            st.write(result.get("missing_skills", []))

        except Exception as e:
            st.error(f"Error: {e}")
            st.write(response.text)

    else:
        st.warning("Please upload resume and enter job description")