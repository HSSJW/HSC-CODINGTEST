import sys
input = sys.stdin.readline


dic = dict()

line = input().strip().split(" ")

n = int(line[0])
m = int(line[1])

for i in range(n):
    line = input().strip().split(" ")

    dic[line[0]] = line[1]




for k in range(m):
    print(dic.get(input().strip()))