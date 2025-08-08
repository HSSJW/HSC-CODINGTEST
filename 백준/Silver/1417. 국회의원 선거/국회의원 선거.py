import sys
input = sys.stdin.readline

n = int(input())
pick = list()
result = 0

for i in range(n):
    how = int(input().strip())
    pick.append(how)

max_pick = max(pick)
while pick[0] != max_pick or max_pick in pick[1:]:  # 첫번째 후보가 최대값 && 1번 이후의 후보중에 1번 후보와 같은표 없음
    max_index = pick.index(max_pick, 1)
    pick[max_index] -= 1
    result += 1
    pick[0] += 1
    max_pick = max(pick)

print(result)




