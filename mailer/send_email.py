# mailer/send_email.py

from dotenv import load_dotenv
import os
import resend            # import the module, not a class

load_dotenv()            # load .env into os.environ

# configure the SDK
resend.api_key = os.getenv("RESEND_API_KEY")

"""def send_application_email(to_email: str, subject: str, body: str):
    # build the parameters
    params = {
        "from": os.getenv("RESEND_FROM_EMAIL"),
        "to": [to_email],
        "subject": subject,
        "text": body,
        # or use "html": "<strong>…</strong>"
    }
    # send the email
    response = resend.Emails.send(params)
    print("Resend API response:", response)
    return response """
# Save the generated application letter to a file instead of sending email
def save_application_to_file(letter: str):
    import os
    from datetime import datetime

    # Create a filename based on current date/time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"application_{timestamp}.txt"

    # Save the letter
    with open(filename, "w", encoding="utf-8") as f:
        f.write(letter)

    print(f"✅ Application letter saved successfully as {filename}")
