def solution(x, n):
    answer = []

    i = 1
    while i <= n:
        answer.append(x*i)
        i += 1
    
    return answer