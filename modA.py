import requests 

api_key =  "GJ9XBY2S6TIDBORV"
url_1 = "https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey={api_key}"
url_2 = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}"

response_1 = requests.get(url_1)
response_2 = requests.get(url_2)
print(response_1) # returns <Response [200]> which means it is a successful API call
print(response_2) # returns <Response [200]> which means it is a successful API call

