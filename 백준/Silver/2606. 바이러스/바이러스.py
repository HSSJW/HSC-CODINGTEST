

def dfs(graph, v, visited, count):

    for i in graph[v]:        # i : 현재 노드 번호 // 인접한 노드 순회
        if not visited[i] :   # 인접한 노드 중 미방문 상태인 노드 발견
            visited[i] = True #방문 처리하고
            count += 1        # 오염된 컴퓨터 수 추가

            count = dfs(graph, i, visited, count)



    return count


# --------------------------

n = int(input())
p = int(input())

visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]  # 노드의 연결관계를 저장할 그래프를 n+1개의 빈배열이 저장된 이차원 배열 형태로 선언

count = 0

for i in range(p):   # 0번 인덳스는 비워두고 1~n번 사용
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


## 그래프 생성 완료
visited[1] = True
result = dfs(graph, 1, visited, count)

print(result)