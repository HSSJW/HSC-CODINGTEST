"""
<힌트>
- 사칙연산 -> 4가지 방법 -> dp?
- N을 사칙연산, 이어붙이기를 나열해서 목적숫자를 달성한다.
    - 나열해서 -> 순서가 중요한 방법 선택 -> 순열 -> i가 바깥 반복문
- DP -> 범위가 명확하게 정해진 것들에서 i를 선정한다.

<목표>
- N을 '사용한 횟수'의 최솟값

<접근>
dp[i] : i를 만들 수 있는 최소 연산 횟수 -> number을 i로 사용한 경우
    -> dp[i] = dp[i*N], dp[i+N], dp[i-N], dp[i/N] 중 가장 작은 값
        -> 점화식에 i보다 큰 수가 index로 사용되면 안된다.
        
dp[i] : i번 사용했을 때 만들 수 있는 숫자들의 리스트 -> 이후에 N과 대조해서 맞으면 i가 답
    -> i번 사용했을 때 만들 수 있는 수들 -> i-1번 사용했을 때 사용했던 것들에 대해 모든 방법 시도한 것들


"""

def solution(N, number):

    
    dp = [set() for _ in range(9)] # 0~8인덱스
    
    for x in range(1, 9): # 각각 1~8번 이어붙인 초기값 넣어주기
        tmp = ""
        for _ in range(x):
            tmp += str(N) 
        
        dp[x].add(int(tmp))

    
    # dp[i]는 dp[i-k]와 dp[k] 모든 원소들로 사칙연산한 것 k (1~i-1)
    for i in range(1, 9): # 2번 쓴것부터 쌓아 올리기
        for k in range(1, i):
            
            for a in dp[i-k]:
                for b in dp[k]:

                    plus = a + b
                    minus = a - b
                    mul = a * b

                    if b != 0:
                        div = int(a / b)    
                        dp[i].add(div)

                    dp[i].add(plus)
                    dp[i].add(minus)
                    dp[i].add(mul)
            
    for i, d_set in enumerate(dp):
        
        if number in d_set:
            return i
    
    
    
    return -1




