"""
- 1칸 또는 2칸을 뛸 수 있다 -> 방법이 2개 -> 방법 나열하기 -> dp

<목표>
- 끝에 도달하는 방법이 몇가지인지 알아내기 -> 특정값 i에 관련된 값 1개 구하기 -> dp


dp[i] : i에 도달할 수 있는 방법 수
dp[i] = dp[i-1] + dp[i-2]

dp[0] = 0
dp[1] = 1
dp[2] = 2
"""

def solution(n):
    answer = 0
    dp = [0] * (n+1)
    
    # ✅✅✅✅✅✅✅ n이 점화식에 필요한 2보다 작을 수도 있으므로 예외처리가 필요하다.
    if n == 1:
        return 1
    elif n == 2:
        return 2
    # ✅✅✅✅✅✅✅
    
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    
    
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    
    
    
    return dp[n] 



