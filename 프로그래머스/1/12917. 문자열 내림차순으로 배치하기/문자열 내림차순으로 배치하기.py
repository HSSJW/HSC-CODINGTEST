def solution(s):
    answer = ''
    
    list_s = list(s)
    
    list_s.sort(reverse = True) # 내림차순
    
    answer = ''.join(list_s)
    
    
    return answer