import sys
input = sys.stdin.readline

n = int(input())

number = set()

number = set(input().strip().split(" "))

m = int(input())

iNum = input().strip().split(" ")


for i in iNum:
    if i in number:
        print("1 ", end="")
    else:
        print("0 ", end="")
