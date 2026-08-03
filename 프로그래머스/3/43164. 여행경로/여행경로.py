"""
여행'경로' -> 경로탐색? or dp
항상 "ICN"에서 출발 -> 시작 노드
주어진 항공권을 '모두' 이용해서 경로 구성 -> 백트래킹

<조건>
- 공항 이름 : 알파벳 대문자 3글자
- 공항 개수 : 3 ~ 10000 -> 많지 않다.
- [a, b] : a공항 -> b공항  : 단방향                    -> 정해져있음 -> 경로탐색
- 가능한 경로가 2개 이상일 경우 사전순 앞쪽 경로 선택

<목표>
방문하는 경로를 배열에 담아 리턴

<접근>
- 


"""

from collections import defaultdict

def solution(tickets):
    answer = []
    
    graph = defaultdict(list)
    
    for t in tickets:
        # 단방향 그래프
        graph[t[0]].append(t[1])  # 그래프 연결하고
    
    for start, end in tickets:
        
        graph[start].sort() # 오름차순 정렬 -> 뒤로갈 수록 커지므로 사전순
        

    answer.append("ICN")
        
    
    def dfs(v): # 재귀 dfs에서는 매개변수로 탐색을 시작할 노드를 받는다.
        
        if len(answer) == len(tickets) + 1:
            return True
        
        for i in range(len(graph[v])): # 그래프의 모든 간선 수만큼 반복
            
            nxt = graph[v].pop(i) # 현재 노드에 연결된 노드 중 가장 앞(사전 순 앞)
            answer.append(nxt)
            
            if dfs(nxt):     # dfs 재귀함수이므로 다음 노드에 연결된 경로가 모두 True이면
                return True # 종료하면 된다. : 모든 노드를 방문 완료했다면 여기서 종료
            
            graph[v].insert(i, nxt) # 원래 자리에 다시 삽입해서 현재 노드에서 다른 방향으로 다시 순회 시작할 수 있도록 한다.
            answer.pop() # 이 경로는 실패한 경로이므로 nxt(다음에 가려고 했던 노드)를 제거
            
        return False # i를 거쳐서 가는 길을 실패다.
    
    dfs("ICN")
            
        
    
    
    return answer








