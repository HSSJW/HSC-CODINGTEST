"""
<힌트>
- 모든 음식의 스코빌 지수를 K 이상으로 만들고싶다.
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

- 모든 음식의 스코빌 지수가 K 이상일 때까지 '반복' -> 가장 맵, 두번 째 맵 반복 추출
    -> 힙
    
<조건>
- scoville : 스코빌 지수 리스트

<목표>
- 섞는 최소 횟수


"""

import heapq

def solution(scoville, K):
    answer = 0
    
    
    heapq.heapify(scoville)
    
    while len(scoville) > 1 and scoville[0] < K: # 가장 작은 스코빌지수가 K 이상
        
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        tmp = first + second * 2 # 섞은 음식
        
        heapq.heappush(scoville, tmp)
        answer += 1
        
    if scoville[0] < K:
        return -1
        
    return answer

