import sys
input = sys.stdin.readline

n = int(input())
save = n

i = n

while i >= 4:
    save = i

    while True:
        if (save % 10) != 4 and (save % 10) != 7:  #금민수가 아닌경우
            break
        else: 
            save = int(save/10) #일의자리 제거
            if(save == 0):
                print(i)
                i = 0
                break

    i -= 1


