# 📄 AI Resume Screening System

## 🚀 Overview

The **AI Resume Screening System** is an end-to-end Machine Learning application that evaluates resumes against job descriptions using NLP techniques.
It mimics a real-world **Applicant Tracking System (ATS)** by providing similarity scores, skill matching, and missing skill insights.

This project demonstrates **Data Science + Machine Learning Engineering + Deployment skills**.

---

## 🎯 Key Features

* 📥 Upload Resume (PDF)
* 📝 Input Job Description
* 📊 TF-IDF based similarity score
* 🧠 Skill extraction & matching
* ❌ Missing skill detection
* ⚖️ Hybrid scoring system (TF-IDF + Skill Match)
* ⚡ REST API using FastAPI
* 🎨 Interactive UI using Streamlit
* 🌐 Fully deployed (Backend + Frontend)

---

## 🧠 How It Works

### 1. Resume Parsing

* Extracts text from PDF using `pdfplumber`

### 2. Text Preprocessing

* Lowercasing
* Removing special characters & numbers
* Stopword removal using `nltk`

### 3. TF-IDF Similarity

* Converts text into vectors
* Uses cosine similarity to compute similarity score

### 4. Skill Extraction

* Extracts predefined technical skills from resume & JD

### 5. Skill Matching

* Identifies matched and missing skills
* Computes skill match score

### 6. Hybrid Scoring

Final score is calculated as:

```
Final Score = 0.5 × TF-IDF Score + 0.5 × Skill Match Score
```

---

## 🛠️ Tech Stack

* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, NLTK
* **NLP:** TF-IDF, Cosine Similarity
* **Backend:** FastAPI
* **Frontend:** Streamlit
* **Deployment:**

  * FastAPI → Render
  * Streamlit → Streamlit Cloud
* **Tools:** Git, GitHub

---

## 📁 Project Structure

```
resume_screening/
│
├── app/
│   └── streamlit_app.py
│
├── api/
│   └── main.py
│
├── model/
│   ├── matcher.py
│   └── skill_matcher.py
│
├── utils/
│   ├── text_extraction.py
│   └── text_cleaning.py
│
├── data/
├── requirements.txt
├── start.sh
├── README.md
```

---

## ⚙️ Installation & Setup (Local)

### 1. Clone Repository

```
git clone <your_repo_link>
cd resume_screening
```

### 2. Create Virtual Environment

```
python -m venv venv
```

### 3. Activate Environment

```
venv\Scripts\activate
```

### 4. Install Dependencies

```
pip install -r requirements.txt
```

---

## 🚀 Running Locally

### ▶️ Start FastAPI Backend

```
uvicorn api.main:app --reload
```

### ▶️ Start Streamlit Frontend

```
streamlit run app/streamlit_app.py
```

---

## 🌐 Deployment

### 🔹 Backend (FastAPI on Render)

* Created `start.sh` for production:

```
#!/bin/bash
uvicorn api.main:app --host 0.0.0.0 --port 10000
```

* Build Command:

```
pip install -r requirements.txt
```

* Start Command:

```
bash start.sh
```

👉 Live API:

```
https://ai-resume-screening-f9wk.onrender.com
```

👉 Swagger Docs:

```
https://ai-resume-screening-f9wk.onrender.com/docs
```

---

### 🔹 Frontend (Streamlit Cloud)

* Connected GitHub repository
* Selected file:

```
app/streamlit_app.py
```

* Updated API URL in Streamlit:

```
https://ai-resume-screening-f9wk.onrender.com/predict
```

👉 Live App:

```
https://ai-resume-screening-system-url.streamlit.app/
```

---

## 🔌 API Endpoint

### POST `/predict`

**Input:**

* Resume (PDF file)
* Job Description (text)

**Output:**

```json
{
  "tfidf_score": 39.48,
  "skill_score": 85.71,
  "final_score": 62.59,
  "matched_skills": ["python", "sql", "pandas"],
  "missing_skills": ["tableau"]
}
```

---

## 📊 Sample Output

* TF-IDF Score: 39.48%
* Skill Match Score: 85.71%
* Final Score: 62.59%
* Missing Skill: Tableau

---

## 🔥 Key Highlights

* Built **end-to-end ML system** (data → model → API → UI)
* Solved limitation of TF-IDF using **hybrid scoring**
* Implemented **skill-based matching algorithm**
* Deployed full-stack ML application

---

## 🚀 Future Improvements

* Use **BERT embeddings** for better semantic understanding
* Dynamic skill extraction using NLP models
* Resume ranking system
* Multi-resume comparison
* CI/CD pipeline

---

## 💼 Use Cases

* Automated resume screening for HR
* Resume optimization for job seekers
* ATS system simulation

---

## 👨‍💻 Author

**Ashish Jadhav (AJ)**

---

## ⭐ Conclusion

This project showcases the ability to build, deploy, and present a real-world ML system, combining **Data Science, NLP, Backend Engineering, and Deployment skills**.
