"""
<다익스트라>
- dfs : stack bfs : deque dijkstra : heapq 
- 다익스트라는 최소힙을 사용해서 최소 비용인 것부터 방문한다.
- 기본 다익스트라의 힙에는 (이번 칸에 방문 했을 때 비용, r, c)이다
- 방향성을 함께 기록해야하는 다익스트라에서는 한개를 더 추가해서 방향도 기록한다.
- 또한 비용에서도 해당 칸에 진입했을 때 방향에 따른 비용을 모두 기록해야하므로 3차원 배열을 사용한다.

"""

import heapq
INF = float("inf")

def solution(board):
    answer = 0
    n = len(board)
    
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상 하 좌 우 -> 현재 진행방향 상태도 동일번호
    
    
    # 각 칸까지 갈 때의 특정 칸의 방향마다의 최소비용을 기록
    cost = [[[INF] * 4 for _ in range(n)] for _ in range(n)]  # 3차원 배열
    
    
    heap = []
    
    for direction in (1, 3): # 하, 우 만 가능
        nr, nc = moves[direction][0], moves[direction][1] # 더해줄 좌표
        
        if board[nr][nc] == 0: # 첫칸이 벽인지 아닌지 검사
            
            cost[nr][nc][direction] = 100 # 특정 칸까지으 비용 기록
            heapq.heappush(heap, (100, nr, nc, direction)) # 첫칸 이동은 무조건 직진이므로 100원
    
    
    while heap:
        
        n_cost, r, c, n_dir = heapq.heappop(heap) # 이번 칸까지 비용, 행, 열, 현재 방향
        
        if n_cost > cost[r][c][n_dir]: # 이전에 이 칸에 이 방향으로 더 싸게 온적이 있다면-> 스킵
            continue
            
        for d, move in enumerate(moves): # 상하 좌우 검사
            
            nr, nc = r + move[0], c + move[1]
            
            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                
                new_cost = n_cost
                
                if n_dir == d:
                    new_cost += 100
                else:
                    new_cost += 600
                
                if new_cost < cost[nr][nc][d]: # 기존 최소 비용보다 싸면
                    cost[nr][nc][d] = new_cost
                    heapq.heappush(heap, (new_cost, nr, nc, d))
                    
    return min(cost[n-1][n-1]) # 다익스트라의 리턴 대상을 비용 리스트




