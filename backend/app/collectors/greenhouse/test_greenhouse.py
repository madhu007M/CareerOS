from backend.app.collectors.greenhouse.api import greenhouse_api

jobs = greenhouse_api.fetch_jobs("notion")

print(f"Total Jobs: {len(jobs)}")

print()

for job in jobs[:10]:
    print(job.title)
    print(job.location)
    print(job.url)
    print("-" * 50)