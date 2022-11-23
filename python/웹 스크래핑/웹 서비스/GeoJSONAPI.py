import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API

# JSON API URL 변수에 저장
serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"

# 구글 클라우드에서 받은 개인 API 키
key_API = ""

while True:
    # 지역 입력
    address = input("Enter location: ")
    # 지역을 입력하고 엔터을 치면 탈출
    if len(address) < 1:
        break

    # URL + 지역이름 + API키까지 합쳐줘야 올바른 JSON API를 반환받을 수 있음
    # urlencode메서드는 첫 인자인 query에 {키:값}의 형태로 인자를 전달하면 키=값 의 형태로 데이터를 변환해준다.
    url = serviceurl + urllib.parse.urlencode({"address": address})

    # 최종 완성된 JSON API URL 출력
    print("Retrieving", url)
    # API 본문 open
    uh = urllib.request.urlopen(url)
    # read() -> 파일전체의 내용을 하나의 문자열로 읽어들임 / + 디코딩(유니코드)
    data = uh.read().decode()
    # 문자열로 읽어 들였으니 길이를 계산하면 총 몇개의 문자가 있는지 파악 가능
    print("Retrieved", len(data), "characters")

    # 변수 js에 json.loads -> JSON문서를 포함하는 .read()를 지원하는 텍스트 파일이나 바이너라 파일을 파이썬 객체로 역 직렬화
    try:
        js = json.loads(data)
    # 오류가 발생하면 None으로 초기화 None이 되면 다음구문에서 걸러집니다.
    except:
        js = None
    # JSON안에 status가 없거나, JSON안에 status가 OK가 아니라면
    if not js or "status" not in js or js["status"] != "OK":
        # 오류 메세지와 JSON본문을 출력하고 while로 다시 올라감
        print("==== Failure To Retrieve ====")
        print(data)
        continue

    # json을 str형태로 출력 하겠다 / indent(들여쓰기) 를 4칸 하겠다. 라는 의미입니다.
    print(json.dumps(js, indent=4))

    # JSON은 딕셔너리의 형태이기 때문에 딕셔너리의 접근방법을 써도 무관하다.
    # JSON내부의 result[0] (result는 하나의 리스트로 이루어져 있다) 의 geomeyry의 location의 lat을 저장
    lat = js["results"][0]["geometry"]["location"]["lat"]
    # 동일한 방법으로 geometry의 location의 lag를 저장
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat", lat, "lng", lng)
    # lat 과 lag의 접근방법과 동일하게 formatted_address의 값을 저장
    location = js["results"][0]["formatted_address"]
    print(location)

# Enter location: Korea, Seoul
# Retrieving http://maps.googleapis.com/maps/api/geocode/json?address=Korea%2C+Seoul
# Retrieved 1517 characters
# lat 37.566535 lng 126.9779692
# Seoul, South Korea
