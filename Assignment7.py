# Greet the user
print("Welcome to Space Stocks!")

# Stock Ticker Dictionary of Space Companies
stock_tickers = {'TSLA': 439.67, 'BORGN': 273.43, 'RCKTLB': 523.23, 'SPCE': 22.44,
                 'AJRD': 39.68, 'IRDM': 28.04, 'CSCL': 34.65, 'ASTC': 1.67, 'GOMX': 0.91, 'OHB': 38.65}


while(True):

    # Request ticker for company in all caps
    Ticker = input("Please enter the ticker you wish to review:  ")

    if Ticker in stock_tickers.keys():

        # Print the stock ticker and price based on user entry being true
        print('The stock price for ', Ticker, " is ",
              stock_tickers[Ticker])

        # ask if additional stock review is needed
        next_ticker = input(
            "Would you like to check the stock of another company? (Yes/No) ")

        # check response to determine if another ticker should be reviewed
        if next_ticker == 'No':

            # Close application if response is "No"
            print("Thank you for using Space Stocks!")
            break

    else:

        # Prompt for errors if the ticker does not match the dictionary options
        print("Stock for ", Ticker,
              "could not be found. Please confirm your entry is a space company and enter as all caps.")
# FIN.
