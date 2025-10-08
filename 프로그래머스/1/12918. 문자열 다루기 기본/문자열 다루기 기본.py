def solution(s):
    answer = True
    
    # 문자열 길이가 4 or 6인지 그리고 숫자로만 이루어져 있는지
    
    if not (len(s) == 4 or len(s) == 6) or not s.isdigit():
        answer = False
    
    return answer