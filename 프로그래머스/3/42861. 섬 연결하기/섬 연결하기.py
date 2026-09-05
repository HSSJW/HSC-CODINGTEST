"""
<힌트>
- 섬 -> 노드 / 다리 -> 간선
- 최소의 비용으로 모든 섬이 서로 연결되도록 만드는 -> 노드만 주고 간선 연결
    -> 최소 비용 간선 트리 -> (간선의 개수) == (노드의 개수 + 1)
-       => 최소 비용 간선 트리 -> 크루스칼()

<크루스칼>
1. '비용이 낮은 간선 부터' 순서대로 검사하며 노드에 각각 다른 그룹 번호를 부여한다.
    - 간선을 비용 순서대로 정렬
2. 각각의 노드에서 서로 다른 그룹번호를 부여한다.
3. 간선들을 하나씩 순회하면서 [cost, a, b] 일거니까 a-b의 그룹번호를 기준으로 분기
    - [그룹 번호가 같다 - 이미 연결된 노드] -> 이 간선은 선택되지않고 건너뛴다.
    - [그룹 번호가 다름 - 분리된 그룹이다] -> 간선을 선택하고 그룹번호를 하나로 묶는다.
4. 선택된 간선의 개수가 n-1 or 모든 노드의 그룹 번호가 같아지면 순회 종료
5. 선택된 간선들 cost의 합이 최소 비용 신장 트리의 비용



"""


def solution(n, costs):
    answer = 0 # 선택된 간선들의 비용을 누적
    count = 0 # 선택된 간선의 개수를 누적 -> n-1이 되면 종료된다.
    
    costs.sort(key = lambda x: x[2])
    
    group = dict()
    
    for i in range(n): # n개의 노드에 그룹번호 부여
        group[i] = i    # 0번 노드 초기 그룹번호 -> 0
        
    
    for a, b, cost in costs:
        
        if count == n-1: # 최소 신장 트리의 간선 개수 = 노드개수 - 1
            break
        
        new = group[a]
        old = group[b]
        
        if group[a] == group[b]: # 그룹번호가 같으면 -> 넘기기
            continue
            
        else:
            
            for i in range(n):# b와 같은 그룹을 모두 a그룹으로 바꾼다.
                if group[i] == old:
                    group[i] = new
            
            count += 1
            answer += cost
            
        
    
    return answer



