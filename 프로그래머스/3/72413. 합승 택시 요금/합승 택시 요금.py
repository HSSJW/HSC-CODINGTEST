"""
<힌트>
- 길마다 요금이 책정 -> 다익스트라? (근데 원래 노드별 요금인데 이건 길에 요금) -> 다익스트라는 n1에서 다른 모든 노드로 가는 최소 비용
- 양 방향 비용이 같다고 명시 -> s에서 a, b로 가는 쪽으로만 생각하지말고 a, b에서 s로 가는 경우도 고려


<조건>
- 양방향 그래프 / 양방향 조건 동일
n(3~200) : 노드 개수 -> 200 * 200 해도 40000 이므로 모든 n1 n2 간의 요금을 미리 저장할 수 있다.
s(1~n) : 출발 지점
a(1~n) : a가 가야하는 지점
b(1~n) : b가 가야하는 지점
fares[i] -> [a, b, c] : a-b 사이 요금이 c원
- 만약 합승 vs 안합승 했을 대 안합승이 더 저렴하면 합승 x

<목표>
- a와 b가 모두 귀가하는 최소 요금 = (s->공통) + (공통->a) + (공통+b)


<접근>
0. s에서 n으로 가는 최소 비용 sn 모두 구해서 graph와 별도의 defaultdict에 저장
1. s에서 a, b 각각 가는 비용 sa, sb -> sa + sb = 각자가는 비용 - single_fee
2. a, b에서 n(같이 타고 가서 내리는 곳)까지 가는 비용 -> an, bn을 더한 걸 노드마다 저장 kk -> kk + sn을 하게되면 해당 노드를 거쳐서 지나가는 비용 나온다 -> 이중에 최솟값            - together_fee
3. single_fee와 together_fee를 비교해서 더 작은게 answer

<기록해야하는 것>
1. 노드 마다 a에서 오는 비용 + b에서 오는 비용 = kk + sn 중에 가장 최솟값 => together_fee
2. sa + sb = single_fee

3. 
"""

from collections import defaultdict
import heapq


def solution(n, s, a, b, fares):
    
    graph = defaultdict(list)
    
    for fare in fares:
        v1, v2, fee = fare
        
        graph[v1].append((fee, v2)) # (요금, 연결노드)
        graph[v2].append((fee, v1)) # 양방향 요금 동일
    
    
    n1_n2_dist = defaultdict(list) # n1_n2_dist[n1] = [(두 노드 사이의 최소 비용, n2)]
    # n1 n2 사이의 거리를 모두 구해서 저장하기
    
    # n1 n2사이의 최소 비용 구해서 리턴
    def dajikstra(n1):
        
        heap = [(0, n1)] # (n1->n2 비용, n2)
        dist = [float('inf')] * (n+1)
        
        dist[n1] = 0
        
        while heap:
            
            fee, node = heapq.heappop(heap)
            
            if fee > dist[node]: # 현재 경로로 node까지 온 비용이 dist[node](이미 node까지 온적 있는데 이 비용보다 비쌀 때) -> 이 경로는 검사할 필요가 없다 -> 다음 순회로
                continue
            
            
            for n_fee, nxt in graph[node]:
                
                move_fee = fee + n_fee #nxt노드로 이동했을 경우의 비용
                
                if dist[nxt] > move_fee: # (node->nxt)가 (n1->nxt)의 최소 비용인 경우
                    dist[nxt] = move_fee # (n1 -> nxt) 비용 최솟값을 초기화
                    
                    heapq.heappush(heap, (move_fee, nxt)) # 다익스트라에서는 nxt노드까지 가는 최소 비용을 힙큐에 넣어준다.
        
        return dist # n1->n2를 리턴 
    
    
    # 우선 a b s 에서 각 노드까지의 최소 비용 모두 구해서 저장하기
    
    s_dist = dajikstra(s) # [n] = (s->n) 비용
    a_dist = dajikstra(a)
    b_dist = dajikstra(b)
    
    # 어짜피 s는 비용 0으로 처리되므로 각자 가는 비용을 따로 체크할 필요가 없다. -> 합승도착지가 s인 것으로 고려
#     single_fee = s_dist[a] + s_dist[b] # 각자 가는 비용
    
    min_fee = float('inf')
    
    # s_dist[n] + a_dist[n] + b_dist[n] 가 최소가 되어야한다.
    
    for i in range(n+1):
        new = s_dist[i] + a_dist[i] + b_dist[i]
        
        if min_fee > new: # 최소비용 갱신
            min_fee = new
    
    
    
    return min_fee



