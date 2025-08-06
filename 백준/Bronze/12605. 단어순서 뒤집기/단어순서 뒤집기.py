n = int(input())

for i in range(n):
    str1 = input().split(" ") # 띄어쓰기로 분리
    str1.reverse()
    resultStr = " ".join(str1)

    print(f'Case #{i+1}: {resultStr}')
