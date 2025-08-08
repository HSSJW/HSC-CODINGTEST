import sys
input = sys.stdin.readline
from collections import deque


n = int(input())

deq = deque()

# 덱
# append 뒤에서 추가
# appendleft  앞에서 추가
# pop 뒤에서 제거
# popleft 앞에서 제거
# insert(인덱스, 값)
# count(값) 특정값 개수 세기

for i in range(n):
    line = input().strip().split(" ")

    cmd = line[0]


    if cmd == "push_front":
        deq.appendleft(int(line[1]))
    elif cmd == "push_back":
        deq.append(int(line[1]))
    elif cmd == "pop_front":
        if len(deq) == 0:
            print("-1")
        else:
            print(deq.popleft())
    elif cmd == "pop_back":
        if len(deq) == 0:
            print("-1")
        else:
            print(deq.pop())
    elif cmd == "size":
        print(f'{len(deq)}')

    elif cmd == "empty":
        if len(deq) == 0:
            print("1")
        else:
            print("0")
    elif cmd == "front":
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[0])
    elif cmd == "back":
        if len(deq) == 0:
            print("-1")
        else:
            print(deq[len(deq)-1])
