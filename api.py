import requests 

api_key =  "GJ9XBY2S6TIDBORV"
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

response = requests.get(url) 
print(response) 
# made a successful API call (ready to extract the required forex data)
data = response.json() 
# returns nested dictionary in a json object
print(data)

USDtoSGD_Exchange_Rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']
# Used to find the exchange rate from USD to SGD found in the nested dictionary

def convertUSDtoSGD(USD):
    """
    - converts USD to SGD
    - one parameter required: USD
    """
    return USD * 1.37659


