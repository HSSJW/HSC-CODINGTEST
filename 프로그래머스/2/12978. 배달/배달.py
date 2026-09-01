"""
- 딱봐도 노드-간선 -> 그래프문제
- N개 마을중 K시간(비용) 이하로 배달 가능한 가능 -> BFS
    + 간선마다 비용이 다르다 -> 다익스트라

<조건>
- [a, b, c] : a-b 비용이 c

<접근>
- 비용이 K이하여야 하므로 탐색하면서 비용 누적해야함
- 메서드를 따로 분리해서 가능한지 검사

"""

from collections import defaultdict
import heapq

def solution(N, road, K):
    answer = 0

    graph = defaultdict(list)
    
    for a, b, c in road: # (비용, 상대노드) 양방향 그래프 생성
        
        graph[a].append((c, b))
        graph[b].append((c, a))
    
    
        
    heap = [(0, 1)] # (누적 비용, 노드 번호)
    costs = [float('inf')] * (N+1)
    costs[1] = 0
    
    while heap:

        fee, node = heapq.heappop(heap)
        
        
        if fee > costs[node]: # 같은 노드를 재방문하려는 시도 차단
            continue

        for nxt_fee, nxt in graph[node]:
            new_fee = fee + nxt_fee # nxt노드로 가면 누적비용

            if new_fee < costs[nxt]:
                costs[nxt] = new_fee # 최소 누적비용 갱신

                heapq.heappush(heap, (new_fee, nxt))
                
    for cost in costs:
        if cost <= K:
            answer += 1
        
    
    return answer