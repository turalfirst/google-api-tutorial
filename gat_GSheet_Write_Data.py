from Google import Create_Service

CLIENT_SECRET_FILE = "client_secret_file.json"
SHEET_API_NAME = 'sheets'
SHEET_API_VERSION = 'v4'
SHEET_SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

sheets_service = Create_Service(CLIENT_SECRET_FILE, SHEET_API_NAME, SHEET_API_VERSION, SHEET_SCOPES)

spreadsheet_id = '1QXaCMfd5eycoYa7Q72NXNrVxvuhrJpWTdNXpxI_80WM'
myspreadsheets = sheets_service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
print(myspreadsheets)

worksheet_name = 'TW UK!'
cell_range_insert = 'A1'

values = (

    ('Column A', 'Column B', 'Column C', 'Column D'),
    ('Test 1', 'Test 2', 'Test 3', 'Test 4')

)

value_range_body = {
    'majorDimension': 'ROWS',
    'values': values
}

sheets_service.spreadsheets().values().update(
    spreadsheetId=spreadsheet_id,
    valueInputOption='USER_ENTERED',
    range=worksheet_name + cell_range_insert,
    body=value_range_body
).execute()


values = (

    ('Column A1', 'Column B1', 'Column C1', 'Column D1'),
    ('Test 5', 'Test 5', 'Test 7', 'Test 8')

)

value_range_body = {
    'majorDimension': 'ROWS',
    'values': values
}

sheets_service.spreadsheets().values().append(
    spreadsheetId=spreadsheet_id,
    valueInputOption='USER_ENTERED',
    range=worksheet_name + cell_range_insert,
    body=value_range_body
).execute()