"""
<힌트>
- 의사 코드 -> 시뮬레이션?
- 디딤돌은 고정되어 있고 한칸씩 이동 -> 배열? / 그래프?
- 칸마다 숫자가 정해져있고 이후 밟을 때마다 감소 -> 배열



<의사 코드>
1. 디딤돌마다 숫자가 적혀 있으며 한번 밟을 때 마다 1씩 줄어든다.
2. 디딤돌의 숫자가 0이면 그 다음칸으로 건너 뛰어야한다.
    - 건너뛴 디딤돌 중 처음으로 등장하는 '0이 아닌 디딤돌'로 이동해야한다.


<조건>
- 건너야 하는 사람 수 무제한
- 디딤돌 개수 200,000 -> 2차원 배열 불가능 -> 완전탐색(일반 경로탐색) 불가능
- 한명이 모두 건넌 후에야 다음 사람 시도 가능
- k : 한번에 건너 뛸 수 있는 최대 개수

<목표>
- 최대 몇명 까지 건널 수 있는지 => 중간에 끊기는 첫 구간 등장 전까지

<접근 2>
- stones[i]가 있을 때 stones[i-1] ~ stones[i-k] 까지 모두 stones[i]보다 작은 것
    - 중에서 stones[i-1] >= stones[i-2] ... >= stones[i-k] 인 것

<방법>
dp[i] : stones[i-1] ~ stones[i-k] 중 max

1. stones[i] 보다 stones[i-k] 가 작으면서
2. stones[i-k] >= stones[i-k+1:i] 일 때

여기서 기억해야하는 값은? -> 
dp[i] : 이 칸까지 올 수 있는 수 : stones[i-k:i] 중에서 가장 큰 수

    - max(stones[i-k:i]) <= stones[i]인 경우 -> dp[i] = max(dp[i-k:i])
    -                       >                 -> dp[i] = stones[i]


dp[i] : max(dp[i-k:i]) 와 stones[i] 중에 더 작은거

"""

from collections import deque
def solution(stones, k):
    answer = 0
    n = len(stones)
    
    dp = [0] * n
    max_dq = deque([])
    
    # 만약 앞에 i-k부터 i-1 까지 모두 자기보다 작으면 중단?
    
    for idx in range(k): # 0 ~ n 까지 미리 초기화
        dp[idx] = stones[idx]
        
        while max_dq and dp[max_dq[-1]] <= dp[idx]: # 가장 오른쪽 값보다 크다 -> 내림차순 깨짐
            max_dq.pop() # 제거
        
        max_dq.append(idx)    

    
    for i in range(k, n):
        
        if max_dq[0] < i - k: # 단조덱의 가장 왼쪽 값이 `윈도우 시작 인덱스`보다 작다면
            max_dq.popleft() # 범위를 벗어났으므로 제거
            
        # 지금 필요한건 i보다 앞쪽 k개의 디딤돌 dp값
        tmp_max = dp[max_dq[0]] # 내림차순 단조덱읜 [0]번 -> 최댓값
        
        dp[i] = min(tmp_max, stones[i])

        # dp[i]의 값을 기준으로 인덱스를 덱에 넣어야 하므로 dp[i]의 값이 확정된 후에 덱에 넣기
        # 단조 덱에 push하기 직전에는 반드시  while문으로 정렬 검사
        while max_dq and dp[max_dq[-1]] <= dp[i]:
            max_dq.pop()
        
        max_dq.append(i)
        
    answer = max(dp[n-k:n])
            
    return answer





