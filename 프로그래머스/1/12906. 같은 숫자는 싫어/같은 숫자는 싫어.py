def solution(arr):
    answer = []
    """
    - 연속적으로 나타나는 숫자는 하나만 남기고 제거 -> 순서는 유지
    - 
    
    """
    answer.append(arr[0])
    
    if len(arr) == 1:
        return answer
    
    for i in range(1, len(arr)):
        now = arr[i]
        front = arr[i-1]
        
        if front != now:
            answer.append(now)
        
    
    
    
    return answer