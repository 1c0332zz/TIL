# 영화 제목검색을 이용해 해당 영화의 출연진, 스태프 중 연출진으로 궁성된 목록만 출력
# 응답받은 결과 중 첫번째 영화의 id값을 활용, TMDB에서 해당 영화에 대한 출연진과 스태프 목록을 가져옴 (Get Credits)
# 출연진 중 cast_id 값이 10 미만인 출연진만 추출, 연출진은 부서(department)가 Directing 인 데이터만 추출. cast-> cast_id, crew -> department
# cast-> cast_id, crew -> department 추출된 값을 리스트로

import requests
from pprint import pprint


def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie' # 영화의 제목으로 검색할수 있는 변수를 만들어줌.
    params = {
        'api_key' : 'd2f94df713ea62aabe6d2d6157100a12',
        'language' : 'ko-KR',
        'query' : title # 제목이 필수 키이기 때문에 query를 추가해준다.
    }
    response = requests.get(BASE_URL+path, params).json() # 영화 제목을 검색할 수 있는 변수
    result_dict = {'cast':[], 'crew':[]} # {cast:actors, crew:directors} 형태로 반환할 딕셔너리
    if response['results']: # 영화 제목을 검색할 수 있게 if문 안에 검색을 넣어준다음에
        movie_id = response['results'][0]['id']
        path2 = f'/movie/{movie_id}/credits' # 영화 아이디를 활용해 배우,감독 목록 조회를 생성한다.
        params2 = {
            'api_key' : 'd2f94df713ea62aabe6d2d6157100a12', 
            'language' : 'ko-KR',
            'query' : movie_id
        } 
        response2 = requests.get(BASE_URL+path2, params2).json() # 이 URL을 이용해서 requests 패키지를 이용해, json 데이터를 응답받아, dictionary 형태로 만들어준다.

        for actor in response2['cast']: # ['cast']를 반복하며, 배우 상세정보 조회
            if actor['cast_id'] < 10: # cast_id 값이 10보다 작은 배우의 이름을 result_dict['cast']의 value값으로 추가한다.
                result_dict['cast'].append(actor['name'])
        
        for crew in response2['crew']: # ['crew']를 반복하며, 스텝 상세정보 조회
            if crew['department'] == 'Directing': # department값이 Directing인 감독의 이름을 result_dict['crew']의 value값으로 추가한다.
                result_dict['crew'].append(crew['name'])
        return result_dict
    else:
        return None


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
