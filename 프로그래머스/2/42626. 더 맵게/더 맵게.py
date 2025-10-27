import heapq

def solution(scoville, K):
    answer = 0
    
    """
    가장 낮은 두개의 음식을 섞는다
    가장 낮은 스코빌 + 두번째로 낮은 스코빌*2 -> K이상이 될 때까지 반복
    
    최소 몇번을 섞어야 하는지
    
    1. 현재 스코빌지수(how) >= K?
    2. 안넘는다 -> 섞는다
    3. how = 가장 낮은 스코빌 + 두번째로 낮은 스코빌*2 / answer += 1
    4. 1~3 반복
    
    불가능하면 -1
    """
    
    if K == 0:
        answer = 0
        return answer
    
    heapq.heapify(scoville) # 힙으로 변환 -> heap[0]이 최솟값인걸 보장

    
    while scoville[0] < K: # 최소 스코빌지수(힙의 0번 인덱스(최소값))가 K이상이 될때 까지 반복
        if len(scoville) != 1:
            
            min_scov = heapq.heappop(scoville)
            sec_scov = heapq.heappop(scoville)
            
            heapq.heappush(scoville, min_scov + sec_scov * 2) # 섞기 -> 섞은 음식 제거
            answer += 1
            
        else:
            answer = -1
            break
        
    
    
    return answer