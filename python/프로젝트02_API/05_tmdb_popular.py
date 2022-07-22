import requests
BASE_URL = 'https://api.themoviedb.org/3'
path = '/movie/now_playing'
# api_key 발급받아서 각자 키를 넣어주세요.
params = {
    'api_key': '',
    'language': 'ko-KR'
}

response = requests.get(BASE_URL+path, params=params).json()
print(response)