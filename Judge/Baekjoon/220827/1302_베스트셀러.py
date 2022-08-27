# https://www.acmicpc.net/problem/1302
import sys
sys.stdin = open('1302_베스트셀러.txt')

N = int(input())
dict = {}
for tc in range(N):
    book = input()
    if book not in dict:
        dict[book] = 1
    else:
        dict[book] += 1
# print(dict)

max_book = max(dict.values())

best_book = []
for book, num in dict.items():
    # print(book, num)
    if num == max_book:
        best_book.append(book)

print(sorted(best_book)[0])
