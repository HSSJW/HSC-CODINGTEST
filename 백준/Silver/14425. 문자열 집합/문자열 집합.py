import sys
input = sys.stdin.readline

line = input().strip().split()

n = int(line[0])
m = int(line[1])

n_string = set()
m_string = []
result = 0

for i in range(n):
    n_string.add(input().strip())

for k in range(m):
    text = input().strip()
    if text in n_string:
        result += 1


print(result)

