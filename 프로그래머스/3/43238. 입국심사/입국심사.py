"""
<힌트>
- 심사관 마다 걸리는 시간이 다르다. -> 비용이 다르다.
- 줄서있는 순서대로 심사받는다.
    - 여러개의 심사대가 있다.

- input값의 크기가 엄청나게 크다. -> 이분탐색? 그리디?
    
<조건>
심사대 수 : len(times)


"""

def solution(n, times):
    answer = 0
    
    lo, hi = 1, min(times) * n
    
    def check(mid): # 이 시간으로 통과 가능한지? -> time동안 n명을 처리 가능한지?
        
        count = 0
        
        for time in times:
            
            count += mid // time # 특정 심사관이 mid 시간동안 처리 가능한 인원 수
        
            if count >= n:
                return True
        
        return False
        
        
    while lo <= hi:
        
        mid = (lo + hi) // 2
        
        if check(mid): # 최소를 찾아야하므로 만족하면 왼쪽으로
            answer = mid # 가장 최근에 가능한 걸 확인한 값이 결과
            hi = mid - 1
            
        else:          # 이 조건에서 불가능 했으므로 더 큰 시간 범위로 이동한다.
            lo = mid + 1
            
    
    
    return answer