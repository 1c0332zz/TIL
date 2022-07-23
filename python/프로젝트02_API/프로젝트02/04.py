# 영화제목으로 검색하여 추천 영화 목록 출력 (Search Movies)
# 응답받은 결과 중 첫번째 영화의 id값을 활용해 TMDB에서 추천영화목록을 가져옴(Get Recommendations) = /movie/{movie_id}/recommendations
# 추천 영화 목록을 리스트로 반환하는 함수를 작성

# 검색할수 있는것과 id값을 활용해 목록을 만든다

import requests
from pprint import pprint


def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie' # 영화의 제목으로 검색한다.
    # /movie/{movie_id}/recommendations # 추천 영화목록
    params = {
        'api_key' : 'd2f94df713ea62aabe6d2d6157100a12',
        'language' : 'ko-KR',
        'query' : title # 제목이 필수 키이기 때문에 query를 추가해준다.
    }
    response = requests.get(BASE_URL+path, params).json()
    results = [] # 결과를 출력하기 위한 리스트를 만들어줌
    if response['results']:
        movie_id = response['results'][0]['id'] # 이 문장이 곧 'id' : 496243 <<딕셔너리의 값을 나타냄.
        path2 = f'/movie/{movie_id}/recommendations' # f를 입력해 {}안에 들어갈수있게해줌
        params2 = {
            'api_key': 'e3ebcaf0cb86336e3fa61579f1f0569b',
            'language': 'ko-KR',
            'query': movie_id
        } # 2번째 추천영화목록을 따옴, 왜? 검색어 안에 들어가야하니까
        response2 = requests.get(BASE_URL+path2, params2).json() # 추천영화 변수를 만들어주고
        for i in response2['results']: # 추천영화 안에 정보를 i에 반복시킴
            results.append(i['title']) # title값만 리스트안에 넣어줌
        return results
    else:
        return None

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
