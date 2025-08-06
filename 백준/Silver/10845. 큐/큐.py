import sys
input = sys.stdin.readline
from collections import deque



n = int(input())
que = deque()

for i in range(n):
    cmd, num = None, None

    line = input().strip().split(" ")
    cmd = line[0]


    if cmd == "push":
        num = int(line[1])
        que.append(num)

    elif cmd == "pop":
        if len(que) == 0:
            print(-1)
        else:
            print(que.popleft())

    elif cmd == "size":
        print(len(que))
    elif cmd == "empty":
        if len(que) == 0:
            print(1)
        else:
            print(0)
    elif cmd == "front":
        if len(que) == 0:
            print(-1)
            continue
        print(que[0])
    elif cmd == "back":
        if len(que) == 0:
            print(-1)
        else:
            print(que[len(que)-1])