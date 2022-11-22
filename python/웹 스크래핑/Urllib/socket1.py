import socket

# 아직 아무 데이터하고도 연결되지 않은 파일 핸들
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 인터넷을 통해 소켓을 대상에 연결 (대상은 data.pr4e.org, 80번째 포트)
mysock.connect(("data.pr4e.org", 80))
# Request-Line = Method SP Request-URI SP HTTP-Version CRLF
# encode() = 파이썬은 유니코드로 되어있고 전송할 때 UTF-8형식으로 전송해야 하기 때문
# 내부에서 유니코드를 UTF-8형식으로 인코딩
cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n".encode()
# 데이터(cmd, byte)를 네트워크로 전송
mysock.send(cmd)

while True:
    # 그리고 돌려받은 데이터는 byte
    data = mysock.recv(512)
    if len(data) < 1:
        break
    # decode = UTF-8에서 유니코드로 변경
    print(data.decode(), end="")
# 모든 데이터가 처리되면 종료
mysock.close()


# 결국 이 코드는 소켓을 열고 명령을 보내고 데이터를 받은것
