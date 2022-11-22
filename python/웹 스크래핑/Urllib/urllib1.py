import urllib.request, urllib.parse, urllib.error


# urlopen으로 암묵적으로 처리해서 <head>가 없음
# urllib.request.urlopen라는 핸들을 사용
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
for line in fhand:
    print(line.decode().strip())
