from Google import Create_Service

CLIENT_SECRET_FILE = "client_secret_file.json"
SHEET_API_NAME = 'sheets'
SHEET_API_VERSION = 'v4'
SHEET_SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

sheets_service = Create_Service(CLIENT_SECRET_FILE, SHEET_API_NAME, SHEET_API_VERSION, SHEET_SCOPES)

"""
Blank Spreadsheet File
"""

sheets_file1 = sheets_service.spreadsheets().create().execute()
print(sheets_file1)
dict_keys = sheets_file1.keys()
print(dict_keys)

"""
dict_keys = (['spreadsheetId', 'properties', 'sheets', 'spreadsheetUrl'])
"""


print(sheets_file1['spreadsheetId'])

"""
Advanced Example: Spreadsheets File with some 
"""


sheet_body = {
    'properties': {
        'title': 'My First Google Sheets File',
        'locale': 'en_US',
        'timeZone': 'America/Los_Angeles',
        'autoRecalc': 'HOUR'
    },
    'sheets': [
        {
            'properties': {
                'title': 'TW UK'
            }
        },
{
            'properties': {
                'title': 'TW BEL'
            }
        },
{
            'properties': {
                'title': 'TW AUS'
            }
        },
{
            'properties': {
                'title': 'TW PHP'
            }
        }
    ]
}

sheets_file2 = sheets_service.spreadsheets().create(
    body=sheet_body
).execute()

print(sheets_file2['sheets'])