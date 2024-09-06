import sys
input = sys.stdin.readline

x = int(input())

for i in range(x):
    A = list(map(int, input().split()))
    A.sort() #오름차순

    print(A[-3])