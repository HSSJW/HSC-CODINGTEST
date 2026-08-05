"""
<힌트>
- 중복이 허용된 집합

<조건>
- 최고의 집합
    1. 각 원소의 합이 S
    2. 각 원소의 합이 S 이면서 원소의 곲의 최대가 되는 집합

- n : 10,000 이하 -> 100,000,000 불가능

<목적>
- 최고의 집합을 리스트 형태로 return
- 존재하지 않으면 -> -1

<접근>
- 곱이 최대가 되려면 각 원소들 차이가 최소가 되어야한다.
    - 차이가 최소 -> s/n이 나누어 떨어진다면 s/n 3개
    
10 / 3 = 3.3333   # 내림
4 3 3

10 / 4 = 2.5      # 올림

3, 3, 2, 2

10 / 6 = 1.5xx    # 올림

2, 2, 2, 2, 1, 1

k : 큰수의 개수 q : s//n => 몫
지금 내가 필요로 하는 것은? -> 큰 수(s//n + 1)가 몇개가 되어야 하는가?

s = 큰수 * (큰수의 개수) + 작은 수 * (n - 큰수의 개수)
s = (q + 1) * k + q * (n-k)
s =  qk + k + qn - qk
  = k + qn

k = s - qn
k = s - (s//n) * n
k = 원본 - 몫*n => 나머지

"""

def solution(n, s):
    answer = []
    
    if n > s:
        return [-1]
    
    
    
    if s % n == 0: #나누어 떨어지는 경우
        num = s / n
        for _ in range(n):
            answer.append(num)
    
    else:
        # 큰수 : s // n 작은 수
        bn = s % n # 큰수의 개수
        sn = n - bn # 작은 수의 개수
        
        big = s // n + 1
        small = s // n

        for _ in range(sn):
            answer.append(small)
        
        for _ in range(bn):
            answer.append(big)
            
        
            
    
    
    return answer