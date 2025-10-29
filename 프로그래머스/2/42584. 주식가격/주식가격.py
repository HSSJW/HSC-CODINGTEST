from collections import Counter

def solution(prices):
    answer = []
    
    """
    시간흐름(초단위) -> 순서대로 흐름 -> 스택/큐 , 시뮬레이션?
    prices = 초단위 주식 가격
    
    현재 이후로 해당 인덱스의 가격보다 낮아지는 시간 -> 떨어진 기간
    
    떨어진 기간 -> 자신보다 인덱스가 큰 값들중에 자신보다 작은 것의 개수
    떨
    
    answer = 가격이 떨어지지 않은 기간 -> 자신보다 인덱스가 큰 값들중에 자신 '이상'인 것의 개수
    """
    
#     for i, price in enumerate(prices):     # 자신의 인덱스, 값
#         over = 0
        
#         for j in range(i+1, len(prices)):  # 자신 이후의 값들
            
#             if price <= prices[j]:
#                 over += 1
            
#         answer.append(over) # i번 인덱스의 가격이 떨어지지 않은 기간 저장
    
    n = len(prices)
    
    answer = [0] * n # [0, 0, ..]으로 모두 초기화
    
    for time in range(n):
        
        for i in range(time+1, n): # 자신부터 뒤에 등장한 곳까지만 검사
            
            if prices[time] <= prices[i]:
                answer[time] += 1
            else:
                answer[time] += 1
                break
        
        
        
        

    
    
    return answer