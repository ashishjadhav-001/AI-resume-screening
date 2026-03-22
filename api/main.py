from fastapi import FastAPI, UploadFile, File, Form
import shutil
import os

from utils.text_extraction import extract_text_from_pdf
from utils.text_cleaning import clean_text
from model.matcher import calculate_similarity
from model.skill_matcher import extract_skills, match_skills

app = FastAPI()

UPLOAD_FOLDER = "data"

@app.post("/predict")
async def predict(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    # save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    # process resume
    raw_text = extract_text_from_pdf(file_path)
    cleaned_resume = clean_text(raw_text)
    cleaned_jd = clean_text(job_description)
    
    # scores
    tfidf_score = calculate_similarity(cleaned_resume, cleaned_jd)
    
    resume_skills = extract_skills(cleaned_resume)
    jd_skills = extract_skills(cleaned_jd)
    
    matched, missing, skill_score = match_skills(resume_skills, jd_skills)
    
    final_score = round((0.5 * tfidf_score) + (0.5 * skill_score), 2)
    
    return {
        "tfidf_score": tfidf_score,
        "skill_score": skill_score,
        "final_score": final_score,
        "matched_skills": matched,
        "missing_skills": missing
    }