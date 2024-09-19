import math
import sys
input = sys.stdin.readline

min, max = map(int, input().split())
result = [True] * (max - min + 1)



for i in range(2, int(math.sqrt(max)) + 1):
    isOk = True    #제곱 ㄴㄴ수 인지 구분 True이면 제곱 ㄴㄴ수

    square = i**2

    start = int((min + square - 1) / square) * square # min이상의 가장작은 제곱ㄴㄴ수가 아닌 수

    for j in range(start, max + 1, square): # start ~ max까지 square간격으로 >> 각 제곱수들의 배수(딱봐도 제곱ㄴㄴ수가 아닌 것)은 제외시키기

            result[j - min] = False






print(sum(result))



