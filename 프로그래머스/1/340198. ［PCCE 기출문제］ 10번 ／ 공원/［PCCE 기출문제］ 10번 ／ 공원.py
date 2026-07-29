"""
1. 돗자리 한변의 길이가 5 3 2

<조건>
- -1으로 채워져 있으면 빈칸

<목표>
- 아무런 돗자리 return -1
- 가장 큰 정사각형 돗자리 크기의 한변 길이 -> 가장 큰 가로-세로 길이


-> 
- 투포인터? -> 1. 가로 인덱스 포인터 2. 세로 인덱스 포인터


"""
def solution(mats, park):
    answer = 0
    
    for k in sorted(mats, reverse=True):
        for i in range(len(park) - k + 1): # 왼쪽 모서리 위
            for j in range(len(park[0]) - k + 1):
                
                if all(park[i+di][j+dj] == "-1" for di in range(k) for dj in range(k)):
                    return k
    
    
    return -1