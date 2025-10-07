def solution(x):
    answer = True
    
    x_str = str(x) 
    
    x_list_int = [int(i) for i in x_str]
    
    sum = 0 
    
    for i in x_list_int:
        sum += i
        
        
    if x%sum != 0:
        answer = False
    
    return answer