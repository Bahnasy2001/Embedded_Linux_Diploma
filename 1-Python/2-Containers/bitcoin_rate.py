import requests
# Send a GET request to the CoinDesk API
url=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
# Extract and print the current Bitcoin price in USD
print(url.json()['bpi']['USD'])
# when you run this code, it sends 
# a GET request to the CoinDesk API to fetch the current Bitcoin price in USD and then prints that value.