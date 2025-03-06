import gspread
from google.oauth2.service_account import Credentials

json_key_file = "wossom_service_account.json"
creds = Credentials.from_service_account_file(json_key_file, scopes=["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(creds)

SHEET_NAME = "venda ap"  # Change if using another sheet
sheet = client.open(SHEET_NAME).sheet1  # Open the first worksheet

# Fetch and print only the first row (headers)
headers = sheet.row_values(1)
print("Headers in Google Sheet:", headers)
