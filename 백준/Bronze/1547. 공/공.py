m = int(input()) # 바꾸는 획수
cup = [True, False, False]


for i in range(m):
    a, b = input().split(" ")

    # print(f'{i+1}번째 교환 전 {cup[0]}, {cup[1]}, {cup[2]}')
    temp = cup[int(a)-1]
    cup[int(a)-1] = cup[int(b)-1]
    cup[int(b)-1] = temp
    # print(f'{i+1}번째 교환 후 {cup[0]}, {cup[1]}, {cup[2]}')



for i in range(3):
    if(cup[i]):
        print(i+1)
        break






