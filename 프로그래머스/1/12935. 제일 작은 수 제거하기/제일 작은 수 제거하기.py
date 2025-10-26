def solution(arr):
    answer = []
    
    if len(arr) == 1:
        answer.append(-1)
        
        return answer
    
    max_num = min(arr)
    
    arr.remove(max_num)
    answer = arr
    
    
    return answer