#include <iostream>
#include <vector>   // 그래프 구현
#include <queue>    // 큐구현
#include <algorithm> // 정렬 알고리즘 사용
using namespace std;

int vertex_cnt, edge_cnt, start_vertex_num;
vector<int> list[1001];
bool visit_dfs[1001];
bool visit_bfs[1001];

void dfs(int cur_vertex_num)
{
	cout << cur_vertex_num << " ";
	visit_dfs[cur_vertex_num] = true; //이미 방문했음을 저장
	for (int vertex : list[cur_vertex_num])
	{
		if (!visit_dfs[vertex])    //visit_dfs를 뒤집은것이 true면 >> 방문한적이 없으면
			dfs(vertex);  //방문한적이 없으면 탐색을 이어나간다
	}
}

void bfs(int start_vertex_num)
{
	queue<int> q;  //큐 생성
	q.push(start_vertex_num);
	visit_bfs[start_vertex_num] = true;

	while (!q.empty())
	{
		int cur_vertex_num = q.front();
		q.pop();
		cout << cur_vertex_num << " ";
		for (int vertex : list[cur_vertex_num])
		{
			if (!visit_bfs[vertex])
			{
				visit_bfs[vertex] = true;
				q.push(vertex);
			}
		}
	}
}

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin.tie(NULL);
	cin >> vertex_cnt >> edge_cnt >> start_vertex_num;

	for (int i = 1; i <= edge_cnt; i++)
	{
		int source, dest;
		cin >> source >> dest;
		list[source].push_back(dest);
		list[dest].push_back(source);
	}

	for (int i = 1; i <= vertex_cnt; i++)
	{
		sort(list[i].begin(), list[i].end());  // 벡터의 시작부터 끝까지 정렬
	}

	dfs(start_vertex_num);
	cout << "\n";
	bfs(start_vertex_num);

	return 0;
}