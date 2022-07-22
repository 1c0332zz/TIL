# pip install requests
import requests
# URL로
order_currency = 'BTC'
payment_currency = 'KRW'
URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'
# 요청을 보내서
response = requests.get(URL).json
# 응답 받은 값을 가져온다.
# 객체에서 중요한 두가지 속성과 메서드
print(response, type(response))  # <Response [200]> <class 'requests.models.Response'>

