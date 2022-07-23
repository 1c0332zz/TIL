# - 인기 영화 목록 중 평점이 8점 이상인 영화 목록을 출력합니다.
# - requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
# - 응답 받은 데이터 중 평점(`vote_average`)이 8점 이상인 영화 목록을 리스트로 반환하는 함수를 작성합니다.

import requests
from pprint import pprint


def vote_average_movies():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key' : 'd2f94df713ea62aabe6d2d6157100a12',
    'language' : 'ko-KR'
    }
    response = requests.get(BASE_URL+path, params=params).json()       
    results = response.get('results')
    # pprint(results)                                               # 여기까진 영화 목록 잘 작동
    box = []                                                      # 이제 알았지만 append해줄려면 리스트여야 함 ''안댐
    for i in results:                                             # 영화 목록을 돌려주면서 그중 vote_average만 빼내주기
      if i.get('vote_average') >= 8:                              # 영화의 목록 중 vote_average가 8보다 크거나같으면 엎어주기 // 어디다가? 변수하나 만들어서?
        box.append(i)                                             # 조건이 맞을 때 마다 변수 안에 i를 추가함
    return box                                                    # 들여쓰기 해줘야함 꼭



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가가 8 이상인 영화목록 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(vote_average_movies())
    """
    [{'adult': False,
      'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
      'genre_ids': [28, 12, 878],
      'id': 634649,
      'original_language': 'en',
      'original_title': 'Spider-Man: No Way Home',
      'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                  '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                  '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                  '사상 최악의 위기를 맞게 되는데…',
      'popularity': 1842.592,
      'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
      'release_date': '2021-12-15',
      'title': '스파이더맨: 노 웨이 홈',
      'video': False,
      'vote_average': 8.1,
      'vote_count': 13954},
    ..생략..,
    }]
    """
