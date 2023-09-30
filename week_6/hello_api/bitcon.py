import requests
from pprint import pprint 

try:
    
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    
    request = requests.get(url)
    
    response = request.json()
    
    pprint(response)
    
    print("")
    print("Current price")
    pprint(response['bpi']['USD']['rate_float'])
    
except Exception as e:
    print(e)