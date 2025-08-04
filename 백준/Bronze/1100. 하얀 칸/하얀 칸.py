case = []

for a in range(8):
    case.append(list(input()))



result = 0


for i in range(8):
    for k in range(8):
        if i%2 == 0: # 짝수줄 -> 짝수칸이 흰칸
            if k%2 == 0: # 흰
                if case[i][k] == 'F':
                    result += 1
        else:
            if k%2 == 1:
                if case[i][k] == 'F':
                    result += 1


print(result)