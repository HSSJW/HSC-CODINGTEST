import sys
input = sys.stdin.readline


number = input()


count = [0, 0]   # count[0] = 0 count[1] = 0

for i in range(len(number)):
    if number[i] == '0' and number[i+1] == '1':
        count[0] += 1
    elif number[i] == '1' and number[i+1] == '0':
        count[1] += 1


if(count[0] > count[1]):
    print(count[0])
else:
    print(count[1])
