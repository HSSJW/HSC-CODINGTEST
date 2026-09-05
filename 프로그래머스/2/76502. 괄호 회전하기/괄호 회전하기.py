"""
<힌트>
- 괄호 -> 괄호검사

- 괄호 '문자열' s개 주어질 때
- s를 왼쪽으로 x번 회전 -> 리터럴 회전 -> deque.rotate() -> 왼쪽 회전은 -1
    -> x번 회전은 rotate(-n)하지말고 for문으로 rotate(-1)을 n번 해주기
    
<목표>
- s가 올바른 괄호열이 되게하는 x의 개수

<접근>
- 특정 조건을 반복해서 검사 -> 메서드로 분리 -> 올바른 괄호 문자열인지 검사하는 메서드
- 회전을 반복하면서 넣어보기

"""

from collections import deque

def solution(s):
    n = len(s)
    answer = 0
    
    # 괄호 검사 -> 스택 -> 스택에는 여는 괄호만 들어간다.
    def check(s): # 올바른 괄호 문자열이면 True
        
        opens = set(["(", "{", "["])
        close = set([")", "}", "]"]) # 닫는 문자열들
        
        if s[0] in close: # 처음부터 닫는 괄호
            return False
        
        stack = []

        for c in s:
            
            if c in opens: # 여는 괄호는 바로 push
                stack.append(c)
            
            
            elif not stack: # 괄호가 남았는데 스택에 아무것도 없는 경우
                return False
            
            else: # 닫는 괄호
                
                if c == ')': # 소괄호
                    if stack[-1] == '(': # 짝이 맞다.
                        stack.pop()
                    else:
                        return False
                    
                elif c == '}': # 중괄호
                    if stack[-1] == '{': # 짝이 맞다.
                        stack.pop()
                    else:
                        return False
                    
                elif c == ']': # 대괄호
                    if stack[-1] == '[': # 짝이 맞다.
                        stack.pop()
                    else:
                        return False
                    
        if stack:
            return False
        
        return True
    
    
    queue = deque(s)
    
    for x in range(n):
        copy = queue.copy()
        for _ in range(x): # x번 회전
            
            copy.rotate(-1) # 왼쪽으로 회전
            
        if check("".join(list(copy))): # x번 회전한 문자열을 `올바른 괄호 문자열`이다
            answer += 1
            
        else: # 정상 괄호가 아니다
            continue

    
    return answer


