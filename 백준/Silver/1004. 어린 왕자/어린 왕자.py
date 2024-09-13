import math
import sys
input = sys.stdin.readline

t = int(input())


for i in range(t):
    result = 0
    x_diff = 0
    y_diff = 0

    x1, y1, x2, y2 = map(int, input().split())   # (x1, y1) (x2, y2) 입력받음

    n = int(input())
    for j in range(n):
        a,b,c = map(int, input().split())

        if a >= x1:
            x_diff = a - x1
        else:
            x_diff = x1 - a
        if b >= y1:
            y_diff = b - y1
        else:
            y_diff = y1 - b

        distance1 = math.sqrt(x_diff**2 + y_diff**2) #첫번째 점과 해당 원사이의 거리

        if a >= x2:
            x_diff = a - x2
        else:
            x_diff = x2 - a
        if b >= y2:
            y_diff = b - y2
        else:
            y_diff = y2 - b

        distance2 = math.sqrt(x_diff ** 2 + y_diff ** 2)

        if (distance1 < c and distance2 > c) or (distance1 > c and distance2 < c):
            result += 1

    print(result)
