import requests




try:
    
    data = requests.get('https://catfact.ninja/fact')
    
    print(data.json())
    
except Exception as e:
    print(e)