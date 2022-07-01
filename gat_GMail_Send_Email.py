from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLIENT_SECRET_FILE = "client_secret_file.json"
GMAIL_API_NAME = 'gmail'
GMAIL_API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

gmail_service = Create_Service(CLIENT_SECRET_FILE, GMAIL_API_NAME, GMAIL_API_VERSION, SCOPES)

emailMsg = "Hello, my friend!"
mimeMessage = MIMEMultipart()
mimeMessage['to'] = 'mrturalismayilov@gmail.com'
mimeMessage['subject'] = 'You won'
mimeMessage.attach(MIMEText(emailMsg, 'plain'))
raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

message = gmail_service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
print(message)