"""
자연수 x를 y로 변환

<힌트>
- 사용할 수 있는 연산 -> 방법의 종류 -> dp?
    - x + n
    - x * 2
    - x * 3

<목표>
- x를 3개의 방법을 조합해서 y로 변환 하는 '최소 연산 횟수'

dp[i]가 구하는 대상 그 자체를 의미 -> dp[i] : i를 만들 수 있는 최소연산 횟수

dp[i] = dp[i-n] / dp[i/2](i%2가 0일 때) / dp[i/3] 중 최솟값 + 1

"""

def solution(x, y, n):
    answer = 0
    
    dp = [-1 for _ in range(y+1)]
    
    dp[x] = 0
    print(f'x={x} dp[{x}] = {dp[x]}')
    
    for i in range(x, y+1):
        
        tmp = []
        # print(f'dp[i가 {i}일 때 dp[{i-2}] = {dp[i-2]}')
        if dp[i-n] != -1: # i에서 두칸 앞으로 갔을 때 가능하다 -> +2했다.
            tmp.append(dp[i-n]) # 2 더하기
            
        if i%2 == 0 and dp[int(i/2)] != -1: # 2를 곱해서 i에 오는게 가능하다.
            tmp.append(dp[int(i/2)])
            
        if i%3 == 0 and dp[int(i/3)] != -1: # 3를 곱해서 i에 오는게 가능하다.
            tmp.append(dp[int(i/3)])
            
        
        if tmp: # i번에 올 수 있다
            # print(f'dp[{i}] = {min(tmp) + 1}')
            dp[i] = min(tmp) + 1
        #else:
            #올수 없는 경우는 dp[i]=-1 로 유지
        
    answer = dp[y]
    
    return answer