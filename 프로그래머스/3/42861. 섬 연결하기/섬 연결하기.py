"""
최소비용 + 모든 노드 -> 최소 비용 신장 트리(사이클 x, 최적 간선 ) -> 크루스칼

<크루 스칼>
1. 간선 리스트를 비용 기준 오름차순 정렬
2. 각 노드에 그룹 번호를 부여한다.
    - 그룹 번호를 기록하기 위해 리스트에 기록한다.
3. 간선 연결 리스트를 순회하면서
    3-1. old, new를 만들어서 모든 노드를 순회하면서 old와 같으면 new 그룹으로 바꾼다.

4. 선택한 간선의 개수가 (노드 개수 - 1)이 되면 순회 종료

"""


def solution(n, costs):
    
    costs.sort(key=lambda x: x[2]) 
    
    group = [x for x in range(n)]
    total = 0
    count = 0
    
    
    for a, b, cost in costs:
        
        if group[a] == group[b]: # 같은 그룹이면
            continue             # 아무것도 안한다.
            
        
        old, new = group[a], group[b]
        
        for i in range(n): # old랑 같은 그룹에 있는 노드 (그룹 전체)를 new로 합치기
            if group[i] == old:
                group[i] = new
                
        
        total += cost # 비용 합산 해주고
        count += 1    # 지금 까지 선택된 간선 개수도 증가 시키기
        
        if count == n-1: # 선택된 간선의 개수가 노드의 개수가 (노드의 개수 - 1)
            break
        
    
    
    
    return total