import sys
input = sys.stdin.readline


N, L = map(int, input().split())

result = []
inOk = False

for count in range(L, 101):

    sum = N - (count * (count - 1)) // 2

    if sum % count == 0:
        x = sum // count

        if x >= 0:
            print(" ".join(str(x + i) for i in range(count)))
            inOk = True
            break

if not inOk:
    print(-1)
