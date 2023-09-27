import requests




    
response = requests.get('https://www.google.com')
if response.status_code == 200:
        print("Internet connection")
else:
        print("Some issue occurred")
    

