"""
- 5와 사칙연산 만으로 12를 표현


<목표>
- N과 사칙연산만을 사용해서 표현 할 수 있는 방법 중 N을 가장 적게 사용하는 방법
    -> 직접 해봐야겠네
    -> 규칙이 정해지지 않는 방법4가지(사칙연산)을 선택하며 number에 해당하는 값 구하기
        -> dp

<접근>
dp[i] = N을 사용해서 i를 만들 수 있는 최소 개수 ❌
    -dp[i] = 
        더하기 : dp[i-N] + 1
        빼기   : dp[i+N] + 1
        나누기 : dp[i*N] + 1
        곱하기 : dp[i/N] + 1
        
        중에 최솟 값 -> dp[i]를 구하는데 i보다 큰 수가 사용된다 -> 불가능
    -> 다른 축 (dp[i]의 다른 의미를 찾아보자)
    문제에서 `N을 사용한 횟수는 6 5 4` 
    AND
    dp의 점화식에 사용되는 i는 범위가 명확하게 정해진 것들 중에서 사용한다.
    (N이 9 이상이면 -1을 return) -> N이 사용될 수 있는 횟수가 정해져있다.
    
    -> dp[i]가 N을 i번 사용해서 만들 수 있는 수 종류
    -> 그러면 dp[i]는 숫자 1개가 아니라 set가 되겠군

"""

def solution(N, number):
    answer = 0
    str_N = str(N)
    # dp[i] = N을 i번 사용해서 만들 수 있는 숫자들 종류 -> 종류 이므로 set로 관리
    # set에 들어갈 값들 구하다가 number과 일치하는 숫자 찾으면 현재 i를 리턴
    
    
    # i는 1~8
    dp = [set() for _ in range(9)] # dp[0]은 사용하지 않고 dp[1~8]만 사용한다.
    
    for i in range(1, 9): # 이어붙인 경우를 먼저 넣어주기
        str_num = ''
        
        for j in range(i): # i번 이어붙이기
            str_num += str_N
        # print(f'dp[{i}]에 {str_num}이 추가됩니다.')
        dp[i].add(int(str_num)) # 이어붙인 숫자 5, 55, 555... add하기
        
    
    # print(dp[1])
    # dp[i] = dp[i-n] + - * / dp[n]한 경우를 다 add
    
    for i in range(2, 9): # 1개는 N밖에 없음
        for n in range(1, i):
            for x in dp[i-n]:
                for y in dp[n]:
                    
                    plus = x + y # dp[1] + dp[1]
                    minus = x - y
                    mul = x * y
                    
                    if x >= 0 and y != 0:
                        div = x // y # 나누기 연산에서 나머지는 무시
                        dp[i].add(div)
                        
                    dp[i].add(plus) # set에 추가해주기
                    dp[i].add(minus)
                    dp[i].add(mul)
                    
            
            
    
    for i in range(1, 9):
        for num in dp[i]:
            if num == number:
                return i
    
    
    return -1





