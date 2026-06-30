import streamlit as st
import requests

st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="🗂️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ICON_DOC = """<svg width="34" height="34" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><line x1="10" y1="9" x2="8" y2="9"/></svg>"""
ICON_UPLOAD = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#818cf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>"""
ICON_BRIEFCASE = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#818cf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>"""
ICON_CHECK = """<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg>"""
ICON_X = """<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>"""
ICON_CHART = """<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#818cf8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>"""

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Poppins', sans-serif; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    .hero {
        text-align: center;
        padding: 2.4rem 1rem 2rem 1rem;
        background: linear-gradient(135deg, #4338ca 0%, #6366f1 50%, #818cf8 100%);
        border-radius: 18px;
        margin-bottom: 1.8rem;
        box-shadow: 0 10px 30px rgba(67, 56, 202, 0.35);
    }
    .hero-title {
        display: flex; align-items: center; justify-content: center; gap: 0.7rem;
        color: white; font-weight: 700; font-size: 2.1rem; margin-bottom: 0.5rem;
    }
    .hero p { color: rgba(255,255,255,0.88); font-size: 1.02rem; margin: 0; }

    .section-label {
        display: flex; align-items: center; gap: 0.5rem;
        font-weight: 600; color: #a5b4fc; font-size: 0.92rem;
        text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 0.7rem;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 14px !important;
        border: 1px solid rgba(129,140,248,0.18) !important;
        background: rgba(255,255,255,0.02);
    }

    div.stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #4338ca 0%, #6366f1 100%);
        color: white; font-weight: 600; font-size: 1.05rem; padding: 0.75rem 0;
        border-radius: 10px; border: none;
        box-shadow: 0 6px 16px rgba(67, 56, 202, 0.35);
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 22px rgba(67, 56, 202, 0.45);
        background: linear-gradient(135deg, #3730a3 0%, #4f46e5 100%);
    }

    .metric-card {
        border-radius: 14px; padding: 1.4rem 1rem; text-align: center;
        background: linear-gradient(160deg, rgba(99,102,241,0.12), rgba(99,102,241,0.03));
        border: 1px solid rgba(129,140,248,0.25);
    }
    .metric-card .label {
        display: flex; align-items: center; justify-content: center; gap: 0.4rem;
        font-size: 0.82rem; color: #9ca3af; font-weight: 500;
        text-transform: uppercase; letter-spacing: 0.03em; margin-bottom: 0.4rem;
    }
    .metric-card .value { font-size: 2.1rem; font-weight: 700; color: #a5b4fc; }

    .pill {
        display: inline-flex; align-items: center; gap: 0.35rem;
        padding: 0.4rem 0.9rem; margin: 0.25rem; border-radius: 999px;
        font-size: 0.86rem; font-weight: 500;
    }
    .pill-match { background: rgba(34,197,94,0.12); color: #4ade80; border: 1px solid rgba(34,197,94,0.3); }
    .pill-missing { background: rgba(239,68,68,0.12); color: #f87171; border: 1px solid rgba(239,68,68,0.3); }

    .footer-note { text-align: center; color: #6b7280; font-size: 0.8rem; margin-top: 2.2rem; }
</style>
""", unsafe_allow_html=True)

st.markdown(f"""
<div class="hero">
    <div class="hero-title">{ICON_DOC} AI Resume Screening System</div>
    <p>Upload a resume and a job description to instantly evaluate the match quality</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="medium")

with col1:
    with st.container(border=True):
        st.markdown(f'<div class="section-label">{ICON_UPLOAD} Upload Resume</div>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "Upload Resume (PDF)", type=["pdf"], label_visibility="collapsed",
        )
        if uploaded_file:
            st.success(f"{uploaded_file.name} uploaded")

with col2:
    with st.container(border=True):
        st.markdown(f'<div class="section-label">{ICON_BRIEFCASE} Job Description</div>', unsafe_allow_html=True)
        job_description = st.text_area(
            "Enter Job Description", height=160, label_visibility="collapsed",
            placeholder="Paste the job description here...",
        )

st.write("")
analyze_clicked = st.button("Analyze Resume", use_container_width=True)

if analyze_clicked:
    if uploaded_file is not None and job_description:
        files = {"file": uploaded_file}
        data = {"job_description": job_description}

        with st.spinner("Analyzing resume against job description..."):
            try:
                response = requests.post(
                    "https://ai-resume-screening-f9wk.onrender.com/predict",
                    files=files, data=data,
                )
            except requests.exceptions.RequestException as e:
                st.error(f"Request failed: {e}")
                response = None

        if response is not None:
            if response.status_code != 200:
                st.error(f"Server returned status code {response.status_code}")
                st.code(response.text)
            else:
                try:
                    result = response.json()

                    with st.expander("Raw API Response (debug)"):
                        st.json(result)

                    st.markdown(f'<div class="section-label" style="font-size:1.1rem; margin-top:1rem;">{ICON_CHART} Results</div>', unsafe_allow_html=True)

                    tfidf = result.get("tfidf_score", "N/A")
                    skill = result.get("skill_score", "N/A")
                    final = result.get("final_score", "N/A")

                    m1, m2, m3 = st.columns(3)
                    with m1:
                        st.markdown(f'<div class="metric-card"><div class="label">TF-IDF Score</div><div class="value">{tfidf}%</div></div>', unsafe_allow_html=True)
                    with m2:
                        st.markdown(f'<div class="metric-card"><div class="label">Skill Match Score</div><div class="value">{skill}%</div></div>', unsafe_allow_html=True)
                    with m3:
                        st.markdown(f'<div class="metric-card"><div class="label">Final Score</div><div class="value">{final}%</div></div>', unsafe_allow_html=True)

                    try:
                        final_val = float(final)
                        st.markdown("<br>", unsafe_allow_html=True)
                        st.progress(min(max(final_val / 100, 0.0), 1.0))
                    except (TypeError, ValueError):
                        pass

                    st.write("")

                    s1, s2 = st.columns(2, gap="medium")

                    with s1:
                        with st.container(border=True):
                            st.markdown(f'<div class="section-label">{ICON_CHECK} Matched Skills</div>', unsafe_allow_html=True)
                            matched = result.get("matched_skills", [])
                            if matched:
                                pills = "".join(f'<span class="pill pill-match">{ICON_CHECK} {s}</span>' for s in matched)
                                st.markdown(pills, unsafe_allow_html=True)
                            else:
                                st.write("No matched skills found.")

                    with s2:
                        with st.container(border=True):
                            st.markdown(f'<div class="section-label">{ICON_X} Missing Skills</div>', unsafe_allow_html=True)
                            missing = result.get("missing_skills", [])
                            if missing:
                                pills = "".join(f'<span class="pill pill-missing">{ICON_X} {s}</span>' for s in missing)
                                st.markdown(pills, unsafe_allow_html=True)
                            else:
                                st.write("No missing skills.")

                except Exception as e:
                    st.error(f"Error parsing response: {e}")
                    st.code(response.text)
    else:
        st.warning("Please upload a resume and enter a job description.")

st.markdown('<div class="footer-note">Powered by AI Resume Screening API</div>', unsafe_allow_html=True)