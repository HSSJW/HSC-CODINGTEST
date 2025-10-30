from collections import deque, defaultdict



    

def solution(n, edge):
    answer = 0
    
    """
    n : 노드의 개수
    간선에 대한 정보가 담긴 2차원 열 [[v1, v2]]
    
    retrun 1번 노드로부터 가장 멀리 떨어진(len(그래프[1])의 max)와 크기가 같은 graph[n]의 개수를 구하기
    """
        
    
    graph = defaultdict(list)
    
    
    for line in edge: # 그래프(트리) 생성
        
        v1 = line[0]
        v2 = line[1]
        
        graph[v2].append(v1)
        graph[v1].append(v2)
        
        
    distance = [-1] * (n+1) # 1번 노드 - n번 노드 사이의 거리를 저장한다
    distance[1] = 0 # 1번부터 사용

    queue = deque([1]) # 1번 노드부터 시작하도록 큐에 넣어둔다


    while queue: # 큐가 모두 빌 때까지
        now_node = queue.popleft()
        count = 0

        for next_node in graph[now_node]: #now_node = 2, 3, 4

            if distance[next_node] == -1:  # next_node = 2 / 3
                queue.append(next_node)
                distance[next_node] = distance[now_node] + 1 # 이전 노드보다 한칸 더 갔다 

    max_distance = max(distance)

    answer = distance.count(max_distance)
    
    
    return answer