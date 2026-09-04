"""
- "ICN" 공항에서 출발해서 a, b 이동 -> 노드/간선? -> 경로탐색
- 항공권 정보가 담긴 2차원 배열 tickets가 매개변수
- 주어진 항공권은 모두 사용 == 모든 간선을 사용

<목표>
- 방문하는 공항 경로를 배열에 담아 return
- 티켓을 모두 소진하는 경로여야한다.
    -  이 경로가 가능한 경로인지 판단해야한다. -> 백트래킹
        -> 가봤다가 막다른 길이면 return하면서 사용한 것들을 복구해야한다.

<접근>
- 경로탐색인데 비용 언급 x / 경로를 가는 방법 -> dfs
- 가능한 경로가 여러개일 경우 알파벳 순서가 앞서는 경로를 선택
    -> 일단 모든 가능한 경로를 2차원 배열로 기록해야겠군
"""

from collections import defaultdict

def solution(tickets):
    answer = []
    n = len(tickets)
    
    graph = defaultdict(list)
    
    
    # a->b 항공권 => 단방향 그래프
    for a, b in tickets:
        graph[a].append(b)
    
    for key in graph.keys():
        graph[key].sort()
        
    # 백트레킹이므로 소비한 것들 기록해야한다.
    #   -> 단방향 그래프이므로 똑같이 딕셔너리로 만들어야한다.
    
    used = defaultdict(list)
    
    for key in graph: # 딕셔너리는 기본으로 key를 리턴
        for _ in range(len(graph[key])):
            used[key].append(False) # key에서 출발하는 티켓만큼 미사용(False)로 기록
    # dfs의 매개변수에는 두 가지
    # 1. 출발점, 2. 누적 경로(답이 되는 상태 값)
    def dfs(start, path):
        
        if len(path) == n + 1: # 노드의 개수 = 간선의 개수 + 1
            return path
            
        for i, nxt in enumerate(graph[start]):
            if not used[start][i]: # 미사용 상태인 티켓만
                
                used[start][i] = True # start-> X 티켓 사용처리
                result = dfs(nxt, path + [nxt]) # 백트레킹에서는 정상 경로인 경우에는 재귀진입
                if result:  # 0, None, False가 아니다이 방향으로 쭉 간게 최종 성공 판정이라면 
                    return result # 최종 결과값을 쭉쭉 전달 - 여기는 path가 담김
                
                else: # 이 경로는 실패했다 -> 소비한 티켓 되돌리기
                    used[start][i] = False
                    
                    
        return False
                
    
    answer = dfs("ICN", ["ICN"])
    
    return answer



