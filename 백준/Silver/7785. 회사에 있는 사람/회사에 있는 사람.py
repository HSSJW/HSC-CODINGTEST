import sys
input = sys.stdin.readline

n = int(input())

enterList = set() #출근자 목록

for i in range(n):
    name, status = input().strip().split(" ")

    if status == "enter":
        enterList.add(name) # 출근처리
    else:
        enterList.discard(name) # 퇴근처리

resultList = sorted(enterList, reverse=True)

for name in resultList:
    print(name)


