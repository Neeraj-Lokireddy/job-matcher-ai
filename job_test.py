from src.job_fetcher.fetcher import fetch_jobs

if __name__ == "__main__":
    API_KEY = "05de988aa849220cfd18924d5f1cc19b0b246a3dc53339a1535782ae240d6ceb"
    jobs = fetch_jobs("data scientist", "Kansas City", API_KEY)

    for i, job in enumerate(jobs, 1):
        print(f"\nJob #{i}")
        print("Title:", job["title"])
        print("Company:", job["company"])
        print("Location:", job["location"])
        print("Link:", job["link"])
        print("Description Preview:", job["description"][:200])
