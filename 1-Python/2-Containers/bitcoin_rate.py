import requests

url=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(url.json()['bpi']['USD'])
# when you run this code, it sends 
# a GET request to the CoinDesk API to fetch the current Bitcoin price in USD and then prints that value.