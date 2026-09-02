"""
롤케이크를 두조각으로 잘라서 동생과 한조각식 나눠먹는다.
- 조각의 크기보다 토핑의 개수 -> 종류의 개수 -> Counter

<조건>
- 동일한 가짓수의 토핑이 올라가면 공평

<목표>
- 공평하게 자르는 방법의 수 / 여러 가지일 수도 있다 -> 다 해봐야함
    - 1,000,000 -> 이차원 배열 불가능
    
<접근>
- 한칸씩 이동하면서 양쪽 슬라이싱해서 Counter로 비교
    - i [:i] [i:]
    - i는 1~(n-2)

"""

from collections import Counter

def solution(topping):
    answer = 0
    n = len(topping)
    
    a = []
    b = topping.copy()
    
    a_counter = Counter(a)
    b_counter = Counter(b)
    
    
    
    
    for top in topping:
        
        a_counter[top] += 1
        b_counter[top] -= 1
        
        if b_counter[top] == 0:
            del b_counter[top]
        
        a_kind = len(a_counter.keys())# a의 종류의 개수
        b_kind = len(b_counter.keys()) # b의 종류의 개수
    
        if a_kind == b_kind:
            # print(f'a_kind = {a_kind} b_kind = {b_kind}')
            answer += 1
    
    return answer