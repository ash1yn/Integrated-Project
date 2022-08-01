import requests 

api_key =  "GJ9XBY2S6TIDBORV"
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

response = requests.get(url)
print(response) # returns <Response [200]> which means it is a successful API call

data = response.json()
print(data)

USDtoSGD_Exchange_Rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']

def convertUSDtoSGD(USD):
    """
    - converts USD to SGD
    - one parameter required: USD
    """
    return USD * USDtoSGD_Exchange_Rate


