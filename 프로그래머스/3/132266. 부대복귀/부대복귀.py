"""
<힌트>
- 유일한 번호로 구분 -> 노드 -> 그래프?
- 이동하는 데 걸리는 시간은 1로 통일 -> 비용이 동일한 -> 다익스트라 x
- 최단 시간 내에 복귀 -> 최단 시간 + 동일 가중치 -> bfs
- 오갈 수 있는 길 -> 양방향 그래프

<조건>
- 적군의 방해로 돌아올 때 길이 끊어진(그래프 연결이 끊어진) 곳이 있을 수 있음
    -> 그래프에서 제거해줘야함

<매개변수>
n : 노드 수
roads : 그래프 연결 정보 [a, b]
sources[i] : i 대원들이 현재 위치한 노드 정보
destination : 복귀해야하는 지점 위치

<목표>
- 대원 별 복귀 가능한 최단 시간
-> 시작점이 여러 개인 bfs -> 방문 기록을 초기화 해야겠네.
- 복귀가 불가능한 부대원은 -1


<시간 초과>
- 특정 노드에서 특정 노드로 이동하는 거리는 모두 동일하다 -> bfs 한번씩 해서 기록해두면 된다


a에서 출발하는데
d와c가 연결되어있는데 mapping[c][a]가 -1보다 크면 여기서 그냥 +1 해주면 된다.
"""

from collections import deque, defaultdict

def solution(n, roads, sources, destination):
    answer = []

    
    graph = defaultdict(list)
    dist = [-1 for _ in range(n+1)]
    
    for a, b in roads:
        
        graph[a].append(b)
        graph[b].append(a)
    
    
    """
    a에서 출발하는데
    d와c가 연결되어있는데 mapping[c][a]가 -1보다 크면 여기서 그냥 +1 해주면 된다.
    나보다 앞쪽에 있는 것들만 검사하면 되겠네
    
    """
    
    def bfs(start): # 탐색을 시작할 노드 번호
        
        dq = deque([start]) # 시작 노드는 먼저 큐에 넣어준다.
        dist[start] = 0 # 시작 노드 위치 초기화

        while dq: # 큐가 빌 때 까지
            
            v = dq.popleft() # 이번에 이동할 노드
            
            if not graph[v]:
                return 
            
            for nxt in graph[v]: # 현재 노드에 연결된 모든 경로 큐에 담기
                
                if dist[nxt] < 0: # 미방문 상태이면
                    dq.append(nxt)
                    dist[nxt] = dist[v] + 1 # 다음 노드는 현재노드 거리 + 1
    
    
    
    
    bfs(destination) 
        
  
    for man in sources:
        
        d = dist[man]
        
        if d == -1:
            answer.append(-1)
        else:
            answer.append(d)
    
    
    
    return answer




