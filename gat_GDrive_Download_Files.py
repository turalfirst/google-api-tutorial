"""
To download files from Google Drive, we'll need MediaIoBaseDownload class
"""
import io
import os
from Google import Create_Service
import pandas as pd
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload # '''  <-------   That is here '''
from google.auth.transport.requests import Request

CLIENT_SECRET_FILE = "client_secret_file.json"
DRIVE_API_NAME = 'drive'
DRIVE_API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

drive_service = Create_Service(CLIENT_SECRET_FILE, DRIVE_API_NAME, DRIVE_API_VERSION, SCOPES)

'''
LOOK FOR ITEMS IN SPECIFIC FOLDER
'''

folder_id = "1AIhbrcglhd9PI2EUSD4Uz6JAC-RhHTFa"

query = f"parents = '{folder_id}'"

response = drive_service.files().list(q=query).execute()
files = response.get('files')
nextPageToken = response.get('nextPageToken')


while nextPageToken:
    response = drive_service.files().list(q=query).execute()
    files = response.get('files')
    nextPageToken = response.get('nextPageToken')

file_ids = []
file_names = ["renamed_test_pic.jpg", "Thesis main paper renamed.docx"] # ''' We can rename files as we want whilst downloading'''

for file in files:
    file_ids.append(file['id'])

for file_id, file_name in zip(file_ids, file_names):

    request = drive_service.files().get_media(fileId=file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)
    done = False

    while not done:

        status, done = downloader.next_chunk()
        print('Download progress {0}'.format(status.progress() * 100))

        fh.seek(0)

    with open(os.path.join('C:\\Users\\mrtur\\OneDrive\\Desktop\\Thesis', file_name), 'wb') as f:
        f.write(fh.read())
        f.close()

