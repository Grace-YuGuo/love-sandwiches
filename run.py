# import gspread library and class Credentials from google.oauth2.service.account function in google.auth library
import gspread
from google.oauth2.service_account import Credentials

# set scope lists the APIs that the program should access in order to run. scope is not changeable so to define SCOPE as constant variable
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
# sales = SHEET.worksheet('sales')
# data =sales.get_all_values()

# define the get_user_data function
def get_sales_data():
    """
    Get sales figures input from the user
    """
    print('Please enter sales data from the last market.')
    print('Data should be six numbers, separated by commas.')
    print('Example: 10,20,30,40,50,60\n')

    data_str=input('Enter your data here:')
    sales_data= data_str.split(',')
    validate_data(sales_data)


    # print(f"sales_data is {sales_data}")
    # print(f"{data_str}")
    # print(f"{sales}")

# define validate_sales_data function
def validate_data(values):
    """
    Inside the try,converts all string values into integers.
    Raisers ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(item) for item in values]
        if len(sales)!=6:
            raise ValueError(
                f'Exactly 6 values required, you provided {len(values)}')
        print(sales)
    except ValueError as e:
        print(f"Invalid data: {e},please try again.\n")
    


get_sales_data()


