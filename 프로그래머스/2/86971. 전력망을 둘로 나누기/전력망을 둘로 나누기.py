from collections import defaultdict, deque

def solution(n, wires):
    answer = 100
    
    """
    나누어진 트리 두개가 비슷한 개수를 가지도록
    graph = {
    1: [3],
    2: [3],
    3: [1, 2, 4],
    4: [3, 5, 6, 7],
    5: [4],
    6: [4],
    7: [4, 8, 9],
    8: [7],
    9: [7]
}
    """

    
    
    # 모든 전선을 하나씩 끊어 보기 -> 트리 생성할 때부터 끊을 전선을 트리에 넣지 않으면 된다
    for i in range(len(wires)):
        
        graph = defaultdict(list) # 리스트형 딕셔너리
        
        for j, wire in enumerate(wires):
            if i == j: # i번째 wire는 끊기
                continue
            
            v1, v2 = wire
            graph[v1].append(v2)
            graph[v2].append(v1)
            
        
        visited = set() # 특정 노드 방문여부를 저장한 셋 -> 중복 불허
        queue = deque([1]) # 큐에 순서대로 인접 노드들은 넣어서 순회할 껀데 1번 노드부터 순회한다
        visited.add(1)  # 1번 노드는 미리 방문처리 해둔다
        
        
        while queue: # 큐에 아무것도 없을 때까지 반복 = 모든 노드 순회를 마쳤을 때
            now_node = queue.popleft()
            
            for next_node in graph[now_node]:
                if next_node not in visited: # 아직 미방문인 노드일 때
                    queue.append(next_node) # 다음 순서로 큐에 등록
                    visited.add(next_node) # 방문처리 
        
        
        side_size = len(visited) # 분리된 한쪽 트리의 노드 개수
        other_side_size = n - side_size
        diff = abs(other_side_size - side_size)
        
        if answer > diff: # 분리된 두 트리의 노드 개수 차이
            answer = diff
    
    return answer






