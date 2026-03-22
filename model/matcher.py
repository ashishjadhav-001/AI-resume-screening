from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, jd_text):
    # combine texts
    texts = [resume_text, jd_text]
    
    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    # cosine similarity
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    
    # convert to percentage
    score = round(float(similarity[0][0]) * 100, 2)
    
    return score