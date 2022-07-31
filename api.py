import requests 

api_key =  "GJ9XBY2S6TIDBORV"
url = "https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey={api_key}"

response = requests.get(url)
print(response) # returns <Response [200]> which means it is a successful API call

print(response.json())

