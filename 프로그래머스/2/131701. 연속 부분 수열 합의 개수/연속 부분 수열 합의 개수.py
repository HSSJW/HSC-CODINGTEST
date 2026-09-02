"""
- 원형 수열 -> 원형 큐 -> deque 회전? / 인덱스 %로 나누기


<목표>
- 원형 수열의 연속 부분 수열의 합으로 만들 수 있는 수의 개수

<접근>
- 1개, 2개, ~ n개 까지 큐를 움직이면서 set에 넣는다.

0~n 인덱스를 고정으로 뽑으면서 큐를 회전시키면?

"""

from collections import deque

def solution(elements):
    answer = 0
    n = len(elements)
    deq = deque(elements)
    
    num_set = set() # 여기에 생성된 숫를 add
    
    
    # 길이가 n인 부분순열 
    for length in range(n):
    
        for _ in range(n): # n번 회전하면서 -> 다 돌고나면 제자리
            
            part = list(deq)[0:length+1] # 길이가 length인 부분순열
            
            num_set.add(sum(part))
            
            deq.rotate(1)
            

    return len(num_set)