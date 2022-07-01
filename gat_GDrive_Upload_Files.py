from Google import Create_Service
import pandas as pd
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request

CLIENT_SECRET_FILE = "client_secret_file.json"
DRIVE_API_NAME = 'drive'
DRIVE_API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

drive_service = Create_Service(CLIENT_SECRET_FILE, DRIVE_API_NAME, DRIVE_API_VERSION, SCOPES)

folder_id = "1AIhbrcglhd9PI2EUSD4Uz6JAC-RhHTFa"

file_names = ["Main Paper - Volatility of Currencies durin Covid-19 (1).docx", "test_pic.jpg"]
mime_types = ["application/vnd.openxmlformats-officedocument.wordprocessingml.document",
              "image/jpeg"]

for file_name, mime_type in zip(file_names, mime_types):
    file_metadata = {

        'name': file_name,
        'parents': [folder_id]

    }

    media = MediaFileUpload('C:/Users/mrtur/OneDrive/Desktop/Thesis/{0}'.format(file_name), mimetype=mime_type)

    drive_service.files().create(
        body=file_metadata,
        media_body = media,
        fields='id'
    ).execute()

