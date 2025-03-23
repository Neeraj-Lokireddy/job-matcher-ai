from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load once (global model)
model = SentenceTransformer('all-MiniLM-L6-v2')  # Small, fast, good

def embed_text(text):
    """Convert text to vector embedding"""
    return model.encode([text])[0]  # return a single vector

def rank_jobs(resume_text, job_list):
    """Rank job descriptions based on similarity to the resume"""
    resume_vec = embed_text(resume_text)

    ranked_jobs = []
    for job in job_list:
        job_desc = job["description"]
        job_vec = embed_text(job_desc)

        score = cosine_similarity([resume_vec], [job_vec])[0][0]
        job["score"] = round(score, 3)
        ranked_jobs.append(job)

    # Sort by highest score
    ranked_jobs.sort(key=lambda x: x["score"], reverse=True)
    return ranked_jobs
