"""

<조건>
- 야근 피로도 = 남은 일의 작업량 **2
- 1시간에 1만큼 처리 가능
- n : 퇴근까지 남은 시간
- work : 0~(len(works)-1)에 대한 남은 작업량

<목표>
- 야근 피로도를 최소화
    - 최소화 -> 완탐?/그리디 -> 20000*1000000 -> 완탐 불가능
- 최소화 하려면? : 제곱해서 야근 피로도를 구하므로 전체적으로 공평하게 낮아지게 해야한다.
    -> 가장 높은 값부터 줄여야한다. -> 최대힙

"""
import heapq

def solution(n, works):
    answer = 0

    works = list(map(lambda x: -x, works))
    
    heapq.heapify(works) # 최소힙
    
    for i in range(n):
        tmp = heapq.heappop(works)
        
        if tmp == 0:
            return 0
        else:
            heapq.heappush(works, tmp+1)
    
    
    answer = sum(list(map(lambda x: x**2, works)))
    return answer





