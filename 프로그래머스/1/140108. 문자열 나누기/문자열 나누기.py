def spliter(s, x, count):
    x_count = 0
    none_x_count = 0
    
    for i in range(0, len(s)): #문자열 📌두번째 글자부터📌 돌면서 검사
        
        if s[i] == x: 
            x_count += 1
        else:
            none_x_count +=1
        
        if x_count == none_x_count:
            
            if (i+1) == len(s): # 마지막 글자일 경우
                return count
            else:
                return spliter(s[i+1:], s[i+1:][0], count) + 1 # 분리되었으면 +1해서 리턴 
                
    
    return count # 분리가 안됐으면 그대로 리턴
        
        

def solution(s):
    
    # x와 x가 아닌 글자들이 나온 횟수 is_x not_x 카운드
    # is_x = not_x 일때 멈추고
    # 지금 까지 읽은 문자열 분리
    # 남은 부분에 대해 반복             -> 재귀함수
    # 분리된 부분의 개수 가 answer
    
    
    if len(s) == 0:
        return 0
    
    x = s[0] # 첫글자
    answer = 1 # 문자열의 개수 1개부터
    
    x_count = 0
    none_x_count = 0
    
    for i in range(len(s)):
        
        if s[i] == x: 
            x_count += 1
        else:
            none_x_count +=1
            
            
        if x_count == none_x_count:
            
        
            if (i+1) == len(s): # 마지막 글자일 경우
                break
                
            else:         # 문자열 분리
                answer += 1
                i += 1
                x = s[i]
                x_count = 0
                none_x_count = 0    
        
    
    return answer