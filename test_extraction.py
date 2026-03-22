from utils.text_extraction import extract_text_from_pdf
from utils.text_cleaning import clean_text
from model.matcher import calculate_similarity
from model.skill_matcher import extract_skills, match_skills

file_path="data/sample_resume.pdf"

job_description = """
Looking for a data analyst with experience in python, excel,
pandas, numpy, and sql power bi and tableau .
"""


raw_text=extract_text_from_pdf(file_path)
cleaned_resume=clean_text(raw_text)

clean_jd=clean_text(job_description)

similarity_score=calculate_similarity(cleaned_resume,clean_jd)

resume_skills = extract_skills(cleaned_resume)
jd_skills = extract_skills(clean_jd)

# skill matching
matched, missing, skill_score = match_skills(resume_skills, jd_skills)

# final hybrid score
final_score = round((0.5 * similarity_score) + (0.5 * skill_score), 2)


print("TF-IDF SCORE:", similarity_score, "%")
print("SKILL MATCH SCORE:", skill_score, "%")
print("MATCHED SKILLS:", matched)
print("MISSING SKILLS:", missing)

print("FINAL SCORE:", final_score, "%")