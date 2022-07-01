from Google import Create_Service

CLIENT_SECRET_FILE = "client_secret_file.json"
DRIVE_API_NAME = 'drive'
DRIVE_API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

drive_service = Create_Service(CLIENT_SECRET_FILE, DRIVE_API_NAME, DRIVE_API_VERSION, SCOPES)




