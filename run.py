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
    while True:
        print('Please enter sales data from the last market.')
        print('Data should be six numbers, separated by commas.')
        print('Example: 10,20,30,40,50,60\n')


        data_str=input('Enter your data here:\n')
        sales_data= data_str.split(',')
        

        if validate_data(sales_data):
            print("Data is valid")
            break

    return sales_data

# define validate_sales_data function
def validate_data(values):
    """
    Inside the try,converts all string values into integers.
    Raisers ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(item) for item in values]
        if len(values)!=6:
            raise ValueError(
                f'Exactly 6 values required, you provided {len(values)}')
        
    except ValueError as e:
        print(f"Invalid data: {e},please try again.\n")
        return False

    return True
    
# define update worksheet data in spreadsheet
def update_worksheet(data,worksheet):
    """
    Update worksheet, add new row with user input or calculation result
    """
    print(f"Updating {worksheet} worksheet...\n")
    worksheet_to_update=SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet updated successfully\n")

# define calculate surplus data function
def calculate_surplus_data(sales_row):
    """
    Compare sales with stock and calculate the surplus for each item type.
    The surplus is defined as the sales figure substracted from the stock:
    -Positive surplus indicates waste
    -Negative surplus indicates extra made when stock was sold out

    """
    print("Calculating surplus data...\n")
    stock=SHEET.worksheet('stock').get_all_values()
    stock_row=stock[-1]

    surplus_data=[]
    for stock,sales in zip(stock_row,sales_row):
        surplus=int(stock)-sales
        surplus_data.append(surplus)

    return surplus_data

# define calculate last five entry average_sales_data
def get_last_five_entries_sales():
    """
    Collects colums of data from sales worksheet, collecting 
    the last five entries for each sandwich and returns the data
    as a list of lists.
    """
    sales=SHEET.worksheet('sales')
    # column=sales.col_values(3)
    # print(column)
    columns=[]
    for int in range(1,7):
        columns.append(sales.col_values(int)[-5:])
    return columns

# define calculate stock data function
def calculate_stock_data(data):
    """
    Calculate the average number of the last five market days for each item 
    and take it plus another 10% as the next market day recommendation
    stock as to encourage sales.
    """
    print("Calculating stock data...\n")
    new_stock_data=[]
    for column in data:
        int_columns=[int(num) for num in column]
        average=sum(int_columns)/len(int_columns)
        stock_num=average*1.1
        new_stock_data.append(round(stock_num))

    return new_stock_data
    print("Calculate stock data completed...")


# def update_surplus_worksheet(data):
#     """
#     Update surplus worksheet, add new row with calculated result
#     """
#     print("Updating surplus worksheet...\n")
#     surplus_worksheet=SHEET.worksheet('surplus')
#     surplus_worksheet.append_row(data)
#     print("surplus worksheet updated successfully\n")

def main():
    """
    Run all program functions
    """
    data=get_sales_data()
    sales_data=[int(num) for num in data]
    update_worksheet(sales_data,'sales')
    new_surplus_data=calculate_surplus_data(sales_data)
    update_worksheet(new_surplus_data,'surplus')
    sales_columns=get_last_five_entries_sales()
    stock_new_row=calculate_stock_data(sales_columns)
    update_worksheet(stock_new_row,'stock')

print("Welcome to Love Sandwiches Data Automation")
main()


