from Google import Create_Service
import pandas as pd
import requests


CLIENT_SECRET_FILE = "client_secret_file.json"
DRIVE_API_NAME = 'drive'
DRIVE_API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

drive_service = Create_Service(CLIENT_SECRET_FILE, DRIVE_API_NAME, DRIVE_API_VERSION, SCOPES)

'''
folder_id = "some gibberish"

query = f"parents = '{folder_id}'"

in this case (when folder id is not needed, so, basically you would like to list all the files and folders in \
 your drive's main page) you'll not use q=query parameter in list method down.
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

pd.options.display.max_rows = 50
pd.options.display.max_columns = 50

for file in files:
    print(file['id'], file['name'])
df = pd.DataFrame(files)
print(df)
