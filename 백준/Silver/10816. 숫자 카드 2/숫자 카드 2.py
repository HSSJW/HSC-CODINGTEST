import sys
input = sys.stdin.readline

n = int(input())

number = list()

number = list(input().strip().split(" "))

m = int(input())

targets = input().strip().split(" ")

count = dict()

for i in number:
    count[i] = count.get(i, 0) + 1 # 개수 1개 카운트


result = list()

for i in targets:
    print(count.get(i, 0), end=" ")