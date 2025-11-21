def solution(s):
    answer = ''
    s = s.lower()
    word_list = s.split(' ')
    
    
    for word in word_list:
        
        if len(answer) != 0:
            answer += ' '
        
        answer += word.capitalize()
        
        
    
    
    return answer