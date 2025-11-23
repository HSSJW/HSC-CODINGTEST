def solution(s):
    answer = 1
    
    i = 0
    
    s_stack = []
    
    for char in s:
        
        if s_stack:
        
            if char == s_stack[len(s_stack) - 1]:
                s_stack.pop()
            else:
                s_stack.append(char)
            
        else:
            s_stack.append(char)
            
            
    if s_stack:
        return 0
            
    
    

    return answer