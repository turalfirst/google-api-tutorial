from Google import Create_Service
import pandas as pd

CLIENT_SECRET_FILE = "client_secret_file.json"
SHEET_API_NAME = 'sheets'
SHEET_API_VERSION = 'v4'
SHEET_SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

sheets_service = Create_Service(CLIENT_SECRET_FILE, SHEET_API_NAME, SHEET_API_VERSION, SHEET_SCOPES)


spreadsheet_id = '1QXaCMfd5eycoYa7Q72NXNrVxvuhrJpWTdNXpxI_80WM'

"""
Example 1. Get Method (Single rrange of values)
"""

response = sheets_service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    majorDimension='ROWS',
    range='TW UK!C3:F7'
).execute()

print(response)
print(response.keys())
print(response['range'] + '\n')
print(response['majorDimension']+ '\n')
print(response['values'])

columns = response['values'][0]
data = response['values'][1:]
df = pd.DataFrame(data,columns=columns)
print(df)


"""
Example 2: Dynamic fetching
"""

response = sheets_service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    majorDimension='ROWS',
    range='TW UK'
).execute()

columns = response['values'][1][1:]
data = [item[1:] for item in response['values'][2:]]
df2 = pd.DataFrame(data,columns=columns)
print(df2)


"""
Example 3. Batch getUpdate
"""

valueRanges_body = [

    'TW UK!C3:F7',
    'TW BEL!C3:F7',
    'TW AUS!C3:F7',
    'TW PHP!C3:F7'

]


response = sheets_service.spreadsheets().values().batchGet(spreadsheetId=spreadsheet_id,
                                                           majorDimension='ROWS',
                                                           ranges=valueRanges_body).execute()
print(response.keys())
print(response['valueRanges'])

dataset = {}



for item in response['valueRanges']:
    dataset[item['range']] = item['values']


print(dataset["'TW UK!C3:F7'"])

df = {}

for indx, k in enumerate(dataset):
    columns = dataset[k][0]
    data = dataset[k][1:]
    df[indx] = pd.DataFrame(data, columns=columns)

print(df)