import requests 
from pathlib import Path

api_key =  "K6YIIIAHV95WGM9K"
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

response = requests.get(url) 
# made a successful API call (ready to extract the required forex data)
data = response.json() 
# returns nested dictionary in a json object

def convertUSDtoSGD(USD):
    """
    - converts USD to SGD
    - one parameter required: USD
    """
    
    
    try:
        
        USDtoSGD_Exchange_Rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        # Used to find the exchange rate from USD to SGD found in the nested dictionary

        return USD * USDtoSGD_Exchange_Rate

    except Exception as e:
        print(f"An error has occurred. \nReason : {e} ")

def exchange_rate():
    """
    - returns the exchange rate extracted from the API
    """
    
   
    try:
        
        USDtoSGD_Exchange_Rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        # Used to find the exchange rate from USD to SGD found in the nested dictionary

        return USDtoSGD_Exchange_Rate

    except Exception as e:
        print(f"An error has occurred. \nReason : {e}")
