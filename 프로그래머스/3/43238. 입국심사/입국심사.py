"""
<힌트>
- 한 심사대는 동시에 한 명만 심사
- 시간? -> 시뮬레이션?
- 가장 앞에 서있는 사람을 비어 있는 곳으로 가서 심사 -> 줄 -> 큐?


<조건>
n : 입국 심사를 기다리는 사람 수
times : 각 심사관이 요구하는 시간

<목표>
- 모든 사람이 심사를 받는데 걸리는 시간의 최솟값
    -> 최소 시간 -> 경로탐색 아니고, dp 살짝 의심가지만 입력이 100,000 이므로 시간복잡도 줄이기
        -> i분에 심사 가능했으면 i+k분은 볼 필요도 없이 가능이다. -> 파라메트릭 서치
        
    
        


"""

def solution(n, times):
    answer = 0
    
    
    # mid시간 안에 n명의 심사가 가능한지
    # mid분에 할 수 사람 수 = mid // times[i] 모두 더하기
    def check(mid):
        
        count = 0
        
        for time in times:
            count += mid // time # mid분에 통과할 수 있는건 소수점 버림
                
            
        if count >= n:

            return True
        else:
            return False
            
    
    
    lo = 1
    hi = max(times) * n # 가장 오래걸리는 사람한테 모두 받기
    
    
    while lo <= hi:
        
        mid = (lo + hi) // 2
        
        
        if check(mid):
            answer = mid
            hi = mid - 1
        else:
            lo = mid + 1
    
    
    return answer

