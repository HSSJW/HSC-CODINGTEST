"""
<힌트>
- 양의 정수 n k진수 변환
- 변환된 수를 조건에 맞는 소수인지 (Prime number)

<조건>
1. 소수 양쪽에 0이 있는경우
2. 왼쪽에 0 오른쪽에 아무것도 없음 -> 가장 오른쪽 숫자
3. 오른쪽에 0 왼쪽에 아무것도 없음 -> 가장 왼쪽 숫자
4. 소수 양쪽에 아무것도 없는 경우 -> 통째로 소수
- 문자로 바꿨을 때 0인 포함되면 안된다.

-> 0이 나오면 잘라서 소수인지 검사

"""
import math

def is_prime(n): # n이 소수인지 검사
    
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False # 소수가 아니다
        
    return True

def convert_base(t, base):
    
    digits = "0123456789"
    result = []
    
    while t > 0:
        t, remainder = divmod(t, base)
        result.append(digits[remainder])
    
    
    return "".join(reversed(result))
    
def solution(n, k):
    answer = 0
    
    tmp = ""# 임시 숫자 문자로 저장
    
    if k != 10:
        conv_n = convert_base(n, k) # k진수로 변환한 문자열 상태 n
    else:
        conv_n = str(n)
    
    for c in conv_n:
        
        if c != "0": # 0이 아니다
            tmp += c
        else: # 0이 등장
            
            if tmp == "": # tmp가 비어있는 경우
                pass
            else:
                
                if is_prime(int(tmp)):

                    answer += 1
                
                tmp = "" # 비우기
                    
        
    if tmp: #마지막이 0 없이 끝나서 남아있는 경우
        if is_prime(int(tmp)):

            answer += 1
        
            
        
        
            
    return answer


