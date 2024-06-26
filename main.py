import os.path

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

SPREADSHEET_ID = '18MYt45bq_UjoAKP-cQjg5nVeyAXaC7lpC_CsUIKXJns'
SAMPLE_RANGE = 'A1:O1000'

def main():
    ##ASKING FOR CREDENTIALS
    creds = None 
    #the json file in the folder stores user's access and refreshes tokens
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    #if there are no valid credentials, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        #save the credientals for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    ##CALLING THE SHEETS API
    try: 
        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SAMPLE_RANGE).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return
        
        print('Started printing')
        for row in values:
            print(row)
    except HttpError as err:
        print(err)

main()