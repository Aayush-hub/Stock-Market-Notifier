from yahoo_fin.stock_info import *                                     #pip install yahoo_fin
import requests_html                                                   #pip install requests_html
from time import time                                                  #in-built module
from datetime import datetime                                          #in-built module
from datetime import date                                              #in-built module
from plyer import notification                                         #pip install plyer
if __name__ == "__main__":
    
    dt = date.today()                                                  #taking current date
    tme = datetime.now().time()                                        #taking current time
    print(f"Today's date is: {dt} ")                                   #printing current date
    print(f"Today's time is: {tme} s")                                 #printing current time
    x = round(get_live_price('dji'),2)                                 #getting real-time price of a Dow-Jones-Industrial-Average
    y = round(get_live_price('ndaq'),2)                                #getting real-time price of a Nasdaq
    print(f"Dow Jones Industrial Average: $ {x}")
    print(f"Nasdaq: $ {y}")
    print("**********Welcome to the Markets***********")
    a1 = input('Enter company name you want to trade \n')              #getting company's name from user
    a = round(get_live_price(a1),2)                                    #getting real-time price of the company
    print(f"Current Stock price of {a1} is: $ {a}")                    #printing current price
    b = int(input("Enter maximum price to be notified: $ "))           #taking maximum price on which user want to sell shares.... to get notified
    c = int(input("Enter stop loss price to be notified: $ "))         #taking stop loss price on which user want to sell shares.... to get notified
    while True:
        q = get_live_price(a1)                                         #getting current price of entered company.
        if q > b:
            notification.notify (                                      #creating desktop notification bar for user to get notified if share price rise...
                title = 'Stock Price has raised',
                message = f"Price of {a1} is: $ {q}",
                timeout = 30
        )
            get_live_price(a1)
            break
        elif q < c:
            notification.notify (                                      #creating desktop notification bar for user to get notified if share price fall...
                title = 'Stock Price has fallen',
                message = f"Price of {a1} is: ${q}",
                timeout = 30
        )
            get_live_price(a1)
            break
   
   ###### printing top gainers and top losers of current or previous day when markets are closed#######
   
    def todayAt (hr, min=0, sec=0, micros=0):                         #converting time format into only hours.
        return tme.replace(hour=hr, minute=min, second=sec, microsecond=micros) 
    if tme>todayAt(1) and tme<todayAt(19):                            #condition of time - when markets are close
        w = get_day_gainers()                                         #getting day gainers
        print(f"Day gainers are: {w}")
        y = get_day_losers()                                          #getting day losers
        print(f"Day losers are: {y}")
        
    ###Other features when markets are closed#####
    
        #get_earnings("Company's name")
        #get_balance_sheet("Company's name")
        #get_analysts_info("Company's name")
        #get_income_statement("Company's name")
        #get_data("Company's name")
    else:
        print("Hope you have a great trading......")                  #printing sweet messages
        print("Thank you for choosing us!!!")   
    
