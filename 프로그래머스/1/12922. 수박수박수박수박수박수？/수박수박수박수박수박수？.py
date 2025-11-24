def solution(n):
    answer = ''
    
    """
    - 문자열 -> 왼쪽부터 순서가 정해져있음
    - 
    """
    
    for i in range(n):
        
        if i % 2 == 1:
            answer += '박'
        else:
            answer += '수'
    
    
    return answer