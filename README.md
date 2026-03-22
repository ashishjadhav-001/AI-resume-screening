# 📄 AI Resume Screening System

## 🚀 Overview

The **AI Resume Screening System** is an end-to-end machine learning application that evaluates a candidate’s resume against a given job description.
It uses **Natural Language Processing (NLP)** techniques to calculate similarity, identify matching skills, and highlight missing skills.

This project simulates a real-world **Applicant Tracking System (ATS)** and demonstrates both **Data Science and Machine Learning Engineering capabilities**.

---

## 🎯 Key Features

* 📥 Upload Resume (PDF format)
* 📝 Input Job Description
* 📊 TF-IDF based similarity scoring
* 🧠 Skill extraction and matching
* ❌ Missing skill detection
* ⚖️ Hybrid scoring system (TF-IDF + Skill Match)
* ⚡ REST API using FastAPI
* 🎨 Interactive UI using Streamlit

---

## 🧠 How It Works

### 1. Resume Parsing

* Extracts text from uploaded PDF resumes using `pdfplumber`

### 2. Text Preprocessing

* Lowercasing
* Removing special characters and numbers
* Stopword removal using `nltk`

### 3. TF-IDF Similarity

* Converts text into numerical vectors
* Calculates similarity between resume and job description using **cosine similarity**

### 4. Skill Extraction

* Extracts predefined skills from both resume and job description

### 5. Skill Matching

* Identifies:

  * ✅ Matched Skills
  * ❌ Missing Skills
* Calculates skill match percentage

### 6. Hybrid Scoring

Final score is calculated using:

```
Final Score = 0.5 × TF-IDF Score + 0.5 × Skill Match Score
```

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn, NLTK
* **NLP Techniques:** TF-IDF, Cosine Similarity
* **Backend:** FastAPI
* **Frontend:** Streamlit
* **Deployment:** Render (API), Streamlit Cloud (UI)

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
│
├── test_extraction.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone <your_repo_link>
cd resume_screening
```

### 2. Create virtual environment

```
python -m venv venv
```

### 3. Activate environment

```
venv\Scripts\activate
```

### 4. Install dependencies

```
pip install -r requirements.txt
```

---

## 🚀 Running the Application

### ▶️ Start FastAPI backend

```
uvicorn api.main:app --reload
```

### ▶️ Start Streamlit frontend

```
streamlit run app/streamlit_app.py
```

---

## 🌐 API Endpoint

### POST `/predict`

**Inputs:**

* Resume file (PDF)
* Job description (text)

**Response:**

```json
{
  "tfidf_score": 39.48,
  "skill_score": 85.71,
  "final_score": 62.59,
  "matched_skills": ["python", "sql"],
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

## 🔥 Future Improvements

* Use **BERT embeddings** for semantic understanding
* Dynamic skill extraction using NLP models
* Resume ranking system
* Support for multiple resumes
* Cloud deployment with CI/CD

---

## 💼 Use Cases

* Automated resume screening for recruiters
* Job seekers optimizing resumes
* HR analytics and hiring systems

---

## 👨‍💻 Author

**Ashish Jadhav (AJ)**

---

## ⭐ Acknowledgement

This project demonstrates practical implementation of **Machine Learning, NLP, and API deployment**, bridging the gap between learning and real-world application.
