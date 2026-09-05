"""
- 경로 -> 경로탐색?
- 공항 이름 : 노드번호
- 3개 이상, 10,000개 이하 -> 경로탐색 기반 완전탐색 가능
- 주어진 항공권은 모두 사용
- 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return
    -> 애초에 탐색할 때 알파벳 순서가 빠른 것인 앞에 오게 정렬해두고 시작하면 통과
    
    
<목표>
- 방문하는 공항 경로를 배열에 담아 return
    - 경로 탐색 문제인데 경로별 비용 x / 최소 비용 x -> dfs
    - 반드시 주어진 것들을 모두 소비해야한다는 조건을 명시 -> 백트래킹
    - 

"""

from collections import defaultdict

def solution(tickets):
    answer = []
    
    graph = defaultdict(list)
    
    # a->b 티켓이므로 단방향 그래프
    for a, b in tickets:
        graph[a].append(b)
    
    # 여러 경로가 있을 경우 알파벳 빠른순으로 방문해야 하기때문에 먼저 방문할 경로 정렬
    for key in graph:
        graph[key].sort()
    
    #소비한 것을 기록해야한다. -> 원본과 똑같이 대응되어야한다.
    # visited에서 모든 노드(칸)마다 똑같이 대응되는 것처럼
    # 노드와 같은 형식으로 만들어야한다.
    used = defaultdict(list)
    for key in graph:
        for _ in range(len(graph[key])):
            used[key].append(False) # graph[key] = value가 key->value 티켓인것처럼
                          # used[key] 는 같은 위치의 목적지로 가는 티켓 소비여부
    
    
    def dfs(airport, path): # 현재 공항, 누적 경로
        
        # 티켓을 다 썻으면 끝 
        if len(path) == len(tickets)+1:
            return path # 끝까지 왔으므로 경로 리턴
        
        for i, nxt in enumerate(graph[airport]): # 현재 공항에서 갈 수 있는 티켓
            
            # airport->nxt행 티켓이므로
            if used[airport][i]: # True -> 이미 (airport->nxt) 티켓 사용 완료
                continue
            
            used[airport][i] = True # 스택에 넣을 때 visited 처리 하는 것처럼 바로 소비
            result = dfs(nxt, path + [nxt]) # result에 들어갈 재귀함수 탈 때 상태 업데이트
            
            if result: # False가 아니라 path가 돌아왔다. -> 성공경로
                return result # 백트래킹에서는 성공경로라면 result를 리턴
            else: # 실패경로다 -> 백트래킹에서 실패하면 복구해야한다.
                used[airport][i] = False
                
        return False
    
    # 백트래킹 문제에서 매개변수 2개는 현재 위치, 누적상태(문제에서 원하는 것)
    answer = dfs("ICN", ["ICN"])
    
    
    
    return answer


