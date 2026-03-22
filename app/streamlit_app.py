import streamlit as st
import requests

st.title("📄 AI Resume Screening System")

# upload file
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# job description input
job_description = st.text_area("Enter Job Description")

if st.button("Analyze Resume"):
    if uploaded_file is not None and job_description:
        
        # send request to FastAPI
        files = {"file": uploaded_file.getvalue()}
        data = {"job_description": job_description}
        
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            files={"file": uploaded_file},
            data=data
        )
        
        result = response.json()
        
        st.subheader("📊 Results")
        st.write(f"TF-IDF Score: {result['tfidf_score']}%")
        st.write(f"Skill Match Score: {result['skill_score']}%")
        st.write(f"Final Score: {result['final_score']}%")
        
        st.subheader("✅ Matched Skills")
        st.write(result["matched_skills"])
        
        st.subheader("❌ Missing Skills")
        st.write(result["missing_skills"])
        
    else:
        st.warning("Please upload resume and enter job description")