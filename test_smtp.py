import os
from dotenv import load_dotenv
import resend

load_dotenv()
resend.api_key = os.getenv("RESEND_API_KEY")

print("Sending test email…")
resend.Emails.send({
    "from": os.getenv("RESEND_FROM_EMAIL"),    # must be your verified sender
    "to": [""],              # ✅ your Resend test email
    "subject": "Test Email from ApplyPilot",
    "text": "Hello! This is a test email using Resend."
})
print("Done!")
