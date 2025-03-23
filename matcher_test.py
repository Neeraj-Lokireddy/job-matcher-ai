from src.resume_parser.parser import parse_resume
from src.job_fetcher.fetcher import fetch_jobs
from src.matcher.matcher import rank_jobs

if __name__ == "__main__":
    # Parse your resume
    resume_data = parse_resume("data/sample_resumes/NEERAJ KUMAR LOKIREDDY resume DS.pdf")
    resume_text = resume_data["raw_text"]

    # Fetch live jobs
    API_KEY = "05de988aa849220cfd18924d5f1cc19b0b246a3dc53339a1535782ae240d6ceb"
    jobs = fetch_jobs("data scientist", "Kansas City", API_KEY)

    # Rank jobs
    ranked = rank_jobs(resume_text, jobs)

    # Show top 5
    for i, job in enumerate(ranked[:5], 1):
        print(f"\nTop Match #{i} - Score: {job['score']}")
        print("Title:", job["title"])
        print("Company:", job["company"])
        print("Location:", job["location"])
        print("Description:", job['description'][:200])
