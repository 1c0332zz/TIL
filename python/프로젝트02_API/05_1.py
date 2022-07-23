import requests
from pprint import pprint

def credits(title):
   
    result_dict = {'cast':[], 'crew':[]}  # {cast:actors, crew:directors} 형태로 반환할 딕셔너리
    urlMaker = 'https://api.themoviedb.org/3/search/movie/d2f94df713ea62aabe6d2d6157100a12/ko-KR'# 1. UrlMaker 인스턴스 객체를 생성한다.
    m_id = urlMaker.movie_id(title) # 2. 입력받은 영화명을 기준으로, 영화번호를 받아온다.
    url = urlMaker.get_url(feature=f'{m_id}/credits')  # 3. 이를 활용해서 배우, 감독 목록 조회 URL을 생성한다.  -> /movie/{movie_id}/credits
    people_dict = requests.get(url).json() # 4. 이 URL을 이용해서 requests 패키지를 이용해, json 데이터를 응답받아, dictionary 형태로 만들어준다.
    # 5. 제대로 접근된 경우에는 key값이 ['id', 'cast', 'crew']이고,
    #    아닌 경우는 key값이 ['success', 'status_code', 'status_message']이다. 
    #    이를 비교해서 key값에 'success'가 있는 경우 None을 반환해주도록 한다.
    if 'success' in people_dict.keys():
        return None
    for actor in people_dict['cast']: # 6-1. people_dict['cast']를 반복하며, 배우 상세정보 조회
        if actor['cast_id'] < 10: # 6-2. cast_id 값이 10보다 작은 배우의 이름을 result_dict['cast']의 value값으로 추가한다.
            result_dict['cast'].append(actor['name'])

    for crew in people_dict['crew']: # 7-1. people_dict['crew']를 반복하며, 스텝 상세정보 조회
        if crew['department'] == 'Directing':# 7-2. department값이 Directing인 감독의 이름을 result_dict['crew']의 value값으로 추가한다.
            result_dict['crew'].append(crew['name'])
    return result_dict # 8. 딕셔너리 값 반환

if __name__ == '__main__':
    pprint(credits('기생충'))
    pprint(credits('id없는 영화'))