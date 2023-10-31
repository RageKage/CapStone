import requests

def main():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"

    user_input = float(input("Enter the amount of Bitcoin you have: "))  
    value = call_bitcoin_api(url, user_input)
    print("The value of your Bitcoin is: ${:.2f}".format(value)) 
def call_bitcoin_api(url, input):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()
        bitcoin_price_in_usd = data['bpi']['USD']['rate_float']
        value = bitcoin_price_in_usd * input
        return value
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Unable to retrieve data from {url}")
        print(e)
        return None

if __name__ == '__main__':
    main()
