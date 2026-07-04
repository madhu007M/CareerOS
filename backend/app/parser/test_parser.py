from backend.app.parser.html_parser import html_parser
from backend.app.parser.job_parser import job_parser

sample_html = """
<div class="job-card">

<h2>Cyber Security Intern</h2>

<p>Bangalore, India</p>

<a href="/apply">Apply</a>

</div>
"""

soup = html_parser.parse(sample_html)

card = soup.find("div")

job = job_parser.parse(card)

print(job)