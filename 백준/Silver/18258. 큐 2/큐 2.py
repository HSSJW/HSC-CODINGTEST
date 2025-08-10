import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
deq = deque()

for i in range(n):
    line = input().strip().split(" ")

    cmd = line[0]

    if cmd == "push":
        num = line[1]
        deq.append(num)
    elif cmd == "pop":

        if len(deq) == 0:
            print("-1")
        else:
            print(deq.popleft())

    elif cmd == "size":
        print(len(deq))
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
            print(deq[len(deq) - 1])
