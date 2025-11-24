def solution(left, right):
    answer = 0
    
    """
    left ~ right
    
    약수의 개수가 
    - 짝수 -> 더하기
    - 홀수 -> 빼기
    
    """
    
    for i in range(left, right+1): # left ~ right+1
        count = 0 # 특정 숫자의 약수의 개수
        
        for k in range(1, int(i/2) + 1):
            
            if i % k == 0: # 약수인 경우
                count += 1
                
        if count % 2 == 0: # 짝수
            answer -= i
        else:
            answer += i
    
    return answer