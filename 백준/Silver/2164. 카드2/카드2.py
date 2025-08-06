import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
number = deque(range(n, 0, -1)) # 큐 사용


while len(number) != 1:
    number.pop() # 오른쪽 끝 삭제
    number.appendleft(number.pop())


print(number[0])
