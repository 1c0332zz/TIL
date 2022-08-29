import sys
sys.stdin = open("11652_카드.txt")

N = int(input())
dict_ = {}

for _ in range(N):
    a = int(input())
    if a not in dict_:
        dict_[a] = 1
    else:
        dict_[a] += 1
# print(dict_)

max_ = max(dict_.values())
result = []
for k, v in dict_.items():
    if v == max_:
        result.append(k)

print(sorted(result)[0])