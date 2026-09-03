"""
<힌트>
- N행 4열 -> [i][0~3]
- 한 행을 내려올 때 한 칸만 밟으면서 내려온다.
    - 같은열을 연속으로 밟는 것은 불가능하다.
    
- 밟는다, 안밟는다 / 1 2 3 4열 중에 하나를 선택하는 것을 나열 -> 방법의 순열 -> dp

<목표>
- 얻을 수 있는 점수의 최대값 -> 마지막 행번호까지 왔을 때의 값 1개 -> dp

<접근>
- dp인데 제한사항에 범위가 정해진게 행번호밖에 없다 -> i는 행번호
- dp[i] : dp[i][0~3] 까지 왔을 때 얻을 수 있는 최댓값

dp[i] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + dp[i][n]

현재 열이 아닌 번호 3개를 어떻게 뽑나? -> [0, 1, 2, 3] - [k]?


"""

def solution(land):
    answer = 0
    
    dp = [[0] * 4 for _ in range(len(land))]
    
    for x in [0, 1, 2, 3]: # 1행 점수 초기화
        dp[0][x] = land[0][x]
    
    for i in range(1, len(land)):
        
        for k in range(0, 4): # 0~3 인덱스
            tmp_list = [0, 1, 2, 3]
            tmp_list.pop(k)
            tmp = tmp_list
            tmp_value = [dp[i-1][x] for x in tmp]

            dp[i][k] = max(tmp_value) + land[i][k]
        
    
    
    
    return max(dp[len(land)-1])