def solution(s):
    answer = True
    stack = []
    
    if len(s) <= 1:
        return False
    
    for char in s:
        stack_size = len(stack)
        
        if char == '(':
            stack.append(char)
        else:
            if stack_size != 0 and stack[stack_size - 1] == '(':
                stack.pop()
            else:
                answer = False
                break
                
    if len(stack) != 0:
        answer = False

    return answer