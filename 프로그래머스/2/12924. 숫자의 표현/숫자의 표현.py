def solution(n):
    answer = 0
    
    start = 1
    end = 1
    sum_num = 1
    
    while start < n // 2 + 1:
        
        if sum_num < n:
            end += 1
            sum_num += end
            
        elif sum_num > n:
            sum_num -= start
            start += 1
            
            
        else:
            answer += 1
            end += 1
            sum_num += end
    
    
    
    return answer + 1