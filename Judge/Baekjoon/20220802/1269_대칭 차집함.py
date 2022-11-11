# 첫째 줄 입력. 어떻게 써먹어야 하는지는 모르겠음
A, B= map(int, input().split())

# a, b값 입력받고 리스트로 변환
a = list(map(int, input().split()))
b = list(map(int, input().split())) 

# 입력받은 a,b를 셋으로 변환해주고 중복되는 숫자 제거 후 set(a)를 빼면 a_에 남은수만 남음
a_ = (set(a) - (set(a) & set(b)))   # 1
b_ = (set(b) - (set(a) & set(b)))   # 3 5 6

# 남은 수를 바탕으로 서로 합쳐주고 len으로 바꿔주면 끝
print(len((list(a_))+(list(b_))))   # 1 3 5 6