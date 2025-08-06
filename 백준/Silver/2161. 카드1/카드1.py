import sys
input = sys.stdin.readline

n = int(input())
numberList = []

for i in range(n):

    numberList.append(n-i)

while len(numberList) != 1:
    print(numberList.pop())
    numberList.insert(0, numberList.pop()) # 맨 위에껄 뽑아서 0번 index에 삽입

print(numberList.pop(), end="")