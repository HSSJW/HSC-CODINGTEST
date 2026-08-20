"""
- 특정 값을 만족하는 방법의 수 -> 목표값(특정칸)은 정해져있다.
- k종류의 동전
- 만들어야하는 값 : n



<목표>
- k종류(k개의 방법)를 조합해서 특정 돈을 만드는 경우의 수 -> dp

dp[i] : i원을 만들 수 있는 종류의 수
    - a b c가 있을 때
    - dp[i] = dp[i-a] + dp[i-b] + dp[i-c] + 만약 money에 i와 같은 수가 있다면 +1

일단 dp[money의 원소] 는 다 채워놔야함
-> money를 중복 조합(combinations_with_replacement(list 중 a 이하의 수, 1~(i/제일 작은 수 를 올림)))으로 뽑아서 
    -> sum()해서 a랑 같은 원소의 개수를 dp[a]에 누적한다.
    
    
dp[i]를 1개만 알아도 뒤에꺼 만들어갈 수 있다.
"""

def solution(n, money):
    answer = 0
    kind = len(money)
    
    if kind <= 1:
        return 1

    
    money.sort() # 오름차순 정렬
    
    dp = [0] * (n+1)

    
    # 초기 dp값 2개만 만들어주면 된다.
    # dp[money[0]] : 무조건 자기 자신 1개
    # dp[money[1]] : money[0] % money[1] != 0 이면 -> 1 아니면 2 
    
    dp[0] = 1
    
        
    for m in money: # 1 2 5
        

        for i in range(m, n+1): # 2 2 3 4 5
        
            # print(f'dp[{i}] += {dp[i-m]}')
            dp[i] = (dp[i] + dp[i-m]) % 1000000007  # 2 - 1 =1

                
            """
            i가 3 -> dp[3-1] dp[3-2] = dp[2] + dp[1]
            i가 4 -> dp[4-1] dp[4-2] = dp[3] + dp[2]
            
            1원
            1. 1
            
            2원
            1. 1 1
            2. 2
            
            3원
            1. 1 1 1
            2. 1 2
            
            
            4원
            1. 1 1 1 1
            2. 1 1 2
            3. 2 2
            
            dp[1] = 1
            dp[2] = dp[1] + 1 = 2
            dp[3] = dp[2] + dp[1] = 3
            dp[4] = dp[4-2] + dp[4-1] = dp[2] + dp[3] = 2 + 3 = 5
            dp[5] = dp[5-1] + dp[5-2] = dp[4] + dp[3] = 
            """
            # dp[4] = dp[4-2] + dp[4-1]
            # dp[4] = dp[2-1] + 1 + dp[3-2] + dp[3-1]
            
    # print(dp)
    
    return dp[n] % 1000000007



