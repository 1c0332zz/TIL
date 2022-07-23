# - 아래의 문서를 활용하여 BTC(비트코인)의 KRW(원) 전일종가를 출력하시오.
# - [https://apidocs.bithumb.com/reference/현재가-정보-조회](https://apidocs.bithumb.com/reference/%ED%98%84%EC%9E%AC%EA%B0%80-%EC%A0%95%EB%B3%B4-%EC%A1%B0%ED%9A%8C)
import requests

order_currency = 'BTC'
payment_currency = 'KRW'

URL = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

response = requests.get(URL) # 응답받은 객체를 가지고옴

# print(response.status_code) # 200
# print(response.text, type(response.text))
# print(response.json()) # <Response [200]> <class 'requests.models.Response'>, 속성과 메서드

data = response.json() # 딕셔너리

print(data.get('data').get('prev_closing_price'))