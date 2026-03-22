# predefined skill list
SKILLS = [
    "python", "sql", "excel", "power bi", "tableau",
    "machine learning", "data analysis", "pandas",
    "numpy", "matplotlib", "seaborn"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []
    
    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)
    
    return list(set(found_skills))


def match_skills(resume_skills, jd_skills):
    matched = list(set(resume_skills) & set(jd_skills))
    missing = list(set(jd_skills) - set(resume_skills))
    
    # score calculation
    if len(jd_skills) == 0:
        score = 0
    else:
        score = round((len(matched) / len(jd_skills)) * 100, 2)
    
    return matched, missing, score