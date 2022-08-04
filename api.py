import requests 
from pathlib import Path

api_key =  "G9O4IFGP94PHD0IR"
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"
summary_report = Path.cwd()/"summary_report.txt"
print(summary_report.exists())

response = requests.get(url) 
print(response)
# made a successful API call (ready to extract the required forex data)
data = response.json() 
# returns nested dictionary in a json object
print(data)

USDtoSGD_Exchange_Rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
# Used to find the exchange rate from USD to SGD found in the nested dictionary

def convertUSDtoSGD(USD):
    try:
        """
        - converts USD to SGD
        - one parameter required: USD
        """
        return USD * USDtoSGD_Exchange_Rate
    except Exception as e:
        print(f"An error has occurred. \nReason : {e} ")

def exchange_rate():
    try:
        """
        - returns the exchange rate extracted from the API
        """
        return USDtoSGD_Exchange_Rate
    except Exception as e:
        print(f"An error has occurred. \nReason : {e}")
