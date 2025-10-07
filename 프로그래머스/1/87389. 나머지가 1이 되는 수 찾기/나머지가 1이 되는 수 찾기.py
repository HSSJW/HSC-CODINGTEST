def solution(n):
    answer = 7

    tmp_n = n - 1
    
    for i in range(2, n):
        if tmp_n % i == 0:
            answer = i
            break
    
    return answer