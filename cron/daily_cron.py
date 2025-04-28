import os
from agent.apply_agent import generate_cover_letter
from mailer.send_email import send_application_email

def run_daily_auto_apply():
    resume_path = "resume.txt"
    job_path = "job.txt"
    with open(resume_path, "r") as r:
        resume = r.read()
    with open(job_path, "r") as j:
        job = j.read()

    letter = generate_cover_letter(resume, job)
   """ send_application_email(
        to_email=os.getenv("TARGET_EMAIL"),
        subject="Daily Auto Job Application",
        body=letter
    )"""
