import requests

MAIILGUN_API_KEY = "MAILGUN_API_KEY_REMOVED"
MAILGUN_API_URL = "https://api.mailgun.net/v3/sandbox5626cb09fe06420086a5d7f40f670cc1.mailgun.org/messages"
FROM_EMAIL_ADDRESS = "postmaster@sandbox5626cb09fe06420086a5d7f40f670cc1.mailgun.org"

def send_email(to_address: str, subject: str, message: str):
  resp = requests.post(
    MAILGUN_API_URL, auth = ("api", MAIILGUN_API_KEY),
    data={
      "from": FROM_EMAIL_ADDRESS,
      "to": to_address,
      "subject": subject,
      "text": message
    }
  )

  if resp.status_code == 200:
    print("Success! Email sent.")

send_email("samy1372@gmail.com", "Test", "This is a test message!")