"""
<힌트>
- 격자 맵
- 상, 하, 좌, 우 이동 가능 / 벽인경우, 맵 벗어나는 경우 고려
- 빠르게(최단 거리)로 (출발->목적지) -> bfs
- 도착하지 못하는 경우도 있다.
- 0은 벽 1은 통로

<목표>
- (1, 1)->(n, m) 가는 `최단거리`
    - 행열로 다룰 것이므로 -1씩 해주기
    (0, 0) -> (n-1, m-1)
- 도착할 수 없을 때에는 -1

<접근>
- 100 * 100 이므로 완탐 가능
    -> bfs로 모든 경로 기록하고 dist[n-1, n-1] 조회하기


"""

from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    que = deque([(0, 0)]) # 시작노드 넣기
    dist = [[-1] * m for _ in range(n)] # 거리 저장
    dist[0][0] = 1 # 출발점 비용
    
    
    while que:
        
        row, col = que.popleft()
        
        for dr, dc in moves:
            nr, nc = row + dr, col + dc # 다음 칸 좌표
            
            # 맵을 벗어나지 않고 통로일 경우
            if 0 <= nr < n and 0 <= nc < m and maps[nr][nc] == 1 and dist[nr][nc] == -1:
                
                dist[nr][nc] = dist[row][col] + 1 # 거리 기록
                que.append((nr, nc)) # 다음에 방문할 칸
    
    
    
    
    return dist[n-1][m-1]


