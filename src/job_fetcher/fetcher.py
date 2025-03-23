import requests

def fetch_jobs(query, location, api_key, num_results=30):
    """Fetch jobs using SerpAPI based on query and location"""
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google_jobs",
        "q": query,
        "location": location,
        "api_key": api_key
    }

    response = requests.get(url, params=params)
    results = response.json()

    jobs = []
    for job in results.get("jobs_results", [])[:num_results]:
        jobs.append({
            "title": job.get("title"),
            "company": job.get("company_name"),
            "location": job.get("location"),
            "description": job.get("description"),
            "link": job.get("related_links", [{}])[0].get("link", "")
        })

    return jobs
