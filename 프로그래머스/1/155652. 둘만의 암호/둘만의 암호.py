def solution(s, skip, index):
    answer = ''
    
    s = list(s) # 문자열 수정을 위해 리스트화
    
    for i in range(len(s)): # s의 모든 문자에 대해 반복
        change_list = []
        
        j = 1
        
        while len(change_list) < index: # index만큼의 문자가 채워졌을 때 
            
            if ord(s[i])+j > ord('z'): # z를 넘어간 경우
                
                j = 0
                s[i] = 'a' # 문자을 a로 바꿔준다
                
                #  a b c d e z   3
                #  1 2 3 4 5 6
            if chr(ord(s[i]) + j) in skip : #이 문자가 스킵문자일 때
                j += 1
            else:
                
                change_char = chr(ord(s[i])+j)
                
                change_list.append(change_char)
                j += 1
                

        answer += change_list[index-1] # 스킵문자를 제외한 index번째 뒤 문자로 변경
        
        

    return answer