from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_skill_match(resume_skills, jd_text):
    jd_text = jd_text.lower()
    match_count = sum(1 for skill in resume_skills if skill in jd_text)
    return match_count / len(resume_skills) if resume_skills else 0


def calculate_similarity(resume_text, jd_text):
    vectorizer = CountVectorizer().fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectorizer)[0][1]
    return similarity


def calculate_final_score(skill_score, similarity, experience):
    exp_score = min(experience / 10, 1)

    return (
        skill_score * 50 +
        similarity * 20 +
        exp_score * 20 +
        0.5 * 5 +
        0.5 * 5
    )