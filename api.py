import requests 
from pathlib import Path

api_key =  "IRBNECTG8CFEVS20"
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
    """
    - converts USD to SGD
    - one parameter required: USD
    """
    return USD * USDtoSGD_Exchange_Rate

    


