# 문제 풀 때 vs code를 그 폴더에서 열어서 활용해주세요~!

# 실제 로컬에서 코드를 작성할 때는 텍스트 파일을 받아서 아래 두 줄 입력!
# 제출하기 전에는 주석처리 부탁드립니다.
import sys
sys.stdin = open("2072_input.txt", "r")

T = int(input()) # 3
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    a = map(int, input().split())
    print(list(a))