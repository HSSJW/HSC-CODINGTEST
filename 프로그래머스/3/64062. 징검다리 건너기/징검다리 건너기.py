"""
<힌트>
- 규칙 -> dp는 아니다.
    - 징검다리 일렬, 칸마다 숫자 -> 배열
    - stones[i] == 0 이면 더이상 밟을 수 없다.
    - 밟을 수 있는(stones[i] > 0) 디딤돌이 여러 개인 경우 무조건 가장 가까운 곳

<조건>
stones : 숫자가 담긴 배열
k : 한번에 건널 수 있는 최대 칸수


<목표>
- 최대 몇명까지 건널 수 있는지? -> 완전 탐색
    -> 200,000개 원소이므로 2차원 배열 불가능하다.
    
<접근>
- k개 구간의 숫자가 모두 
    - 앞, 뒤 숫자보다 작은 경우를 찾는다.
        -> 고정된 너비의 구간을 탐색한다.
        -> 처음부터 끝까지 훑으면서 최저값을 기록한다.

stones[a]를 지났을 때 k개 연속으로 stones[a]보다 작으면 실패
    - stones[a+1] stones[a+2] ... stones[a+k]

<접근3>
- 모든 인덱스에 대해서 stones[i:k]에 대해 


<접근4>
- 구해야되는 대상 -> '최대 몇명이 건널 수 있나?' -> dp, 경로탐색이 아닌  최대/최소 몇명(몇개)? -> 파라메트릭 서치?
- 파라메트릭 서치 이려면 -> 구하는 대상이 k명에서 가능하면 k이하는 검사 할 필요없이 가능하다.
    -> 파라메트릭 서치 -> lo, hi가 구하는 대상이되고 -> 해당 값은 범위를 지문에서 찾는다. 
        -> check를 만족하면 목표쪽(최대 최소)으로 확장한다.
"""

def solution(stones, k):
    answer = 0
            
    lo, hi = 1, max(stones) # 1인 돌이 k연속 있거나, 최대값으로 모두 이루어진 경우
    
    
    # mid명이 건너는게 가능한지 -> stones[i] <= mid 인 돌이 k연속 있는지
    def check(mid):
        
        count = 0
        
        for stone in stones:
            
            if stone < mid:
                count += 1
                
                if count >= k:
                    return False
            else: # 연속이 깨졌으므로 초기화
                count = 0
            
        return True
    
    #---------------------------------------------
    while lo <= hi:
        
        mid = (lo + hi) // 2
        
        if check(mid):
            answer = mid # 최소 mid만큼은 건널 수 있다.
            lo = mid + 1 # 최대값을 구해야 하므로 더 작은 쪽은 버린다.
        
        else:
            hi = mid - 1 # k명 이상은 불가능하다.
        
        
    
    return answer




