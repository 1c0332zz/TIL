import requests 
URL = 'https://api.bithumb.com/public/ticker/ALL_KRW'
response = requests.get(URL).json()
print(response)