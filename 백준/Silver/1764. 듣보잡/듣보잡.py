import sys
input = sys.stdin.readline


n, m = input().split(" ")

n = int(n)
m = int(m)

non_heard = set()
non_see = set()
result = set()

for i in range(n):
    name = input().strip()
    non_heard.add(name)

for k in range(m):
    name = input().strip()

    if name in non_heard:
        result.add(name)

result = sorted(result, reverse=False)

print(len(result))
for name in result:
    print(name)