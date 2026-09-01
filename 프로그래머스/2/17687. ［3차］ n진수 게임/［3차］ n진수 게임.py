"""
- N진수 -> 몫이 0이 될 때까지 remainder(나머지)를 digits[remainder]로 추가해서 뒤집기

<규칙>
1. 숫자를 한 글자씩 말한다.
2. 10부터는 0, 1, 1, 1, 1, 2 ~ 이런식으로 진행

# 숫자를 한 글자씩 말한다 -> 숫자를 문자열로 이어붙여서 한글자씩 출력한다.

<조건>
- 0부터 말한다.
t : 미리 구해야하는 (튜브가 말해야하는) 숫자 개수

"""

def convert_base(base, num): # num를 base진수로 표현한 문자열을 리턴한다.
    
    if num == 0:
        return '0'
    
    rev_conv_num = [] # 문자열을 매번 수정하면 시간복잡도 상승하므로 리스트로 모은다.
    digits = '0123456789ABCDEF'
    
    
    
    while num > 0: # 몫이 0이 될 때까지 나누기
        
        # divmod -> 몫과 나머지를 한번에 리턴
        num, remainder = divmod(num, base) # 몫을 진법으로 나누기
        rev_conv_num.append(digits[remainder])
        
    return "".join(reversed(rev_conv_num)) # 나머지부터 넣었으므로 뒤집기
    
    

def solution(n, t, m, p):
    answer = ''
    
    count = 0 # 지금까지 튜브가 말한 개수 -> t와 같아지면 종료
    # 구해야하는 숫자의 개수(인덱스 + 1) -> (len(str_num) >= t_count)가 되면 종료한다.
    t_count = ((t-1)*m + p) 
    str_num = '' # 이곳에 숫자를 미리 문자열 형태로 이어 붙인다.
    
    num = 0 # 0부터 시작
    while len(str_num) < t_count:
        
        str_num += convert_base(n, num) # num을 n진법으로 변환한 문자열
            
        if len(str_num) >= t_count:
            break
            
        num += 1
            
    print(str_num)
    for i in range(p-1, t_count, m): # 튜브의 순서가 p인데 숫자는 0번부터 있다.
        
        answer += str_num[i]
    
    return answer
# 0110