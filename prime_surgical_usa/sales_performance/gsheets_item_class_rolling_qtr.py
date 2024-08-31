import gspread
from oauth2client.service_account import ServiceAccountCredentials

def gsheet_data_item_class_rolling_qtr():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        r'C:\Users\0xalp\projects\primesurgicalusa\primesurgicalusa-gsheets-7769eb79312f.json', scope
    )
    client = gspread.authorize(creds)
    sheet = client.open("L66_zb_sales_report").get_worksheet(0)
    data = sheet.get_all_records()
    return data