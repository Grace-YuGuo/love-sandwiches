# import gspread library and class Credentials from google.oauth2.service.account function in google.auth library
import gspread
from google.oauth2.service_account import Credentials

# set scope lists the APIs that the program should access in order to run. scope is not changeable that constant variable as SCOPE
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
# declare CREDS /SCOPE_CREDS
CREDS=Credentials.from_service_account_file('creds.json')
SCOPED_CREDS=CREDS.with_scopes(SCOPE)

# declare sheets client and access/open the project spreadsheet
GSPRED_CLIENT=gspread.authorize(SCOPED_CREDS)
SHEET=GSPRED_CLIENT.open('love_sandwiches')

# create variable for sheet data values
sales = SHEET.worksheet('sales')
data =sales.get_all_values()
print(data)



