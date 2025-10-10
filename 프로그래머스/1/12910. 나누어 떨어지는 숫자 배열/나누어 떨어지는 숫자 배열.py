def solution(arr, divisor):
    answer = []
    
    for i in arr:
        if i % divisor == 0: # 나누어 떨어지면
             answer.append(i)
                
    answer.sort()
    
    if not answer:            # answer이 비어있다면
        answer.append(-1)
    
    return answer