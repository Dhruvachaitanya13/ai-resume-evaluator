from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, job_desc):
    """Calculate similarity between resume and job description."""
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_desc])
    similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return similarity_score[0][0]

