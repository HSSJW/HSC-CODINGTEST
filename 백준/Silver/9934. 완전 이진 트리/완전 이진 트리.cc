#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int input[1030];  //초기 입력받기
int numberOfNodes = 0; // 입력한 원소의 개수
vector<int> depth[10]; //최대 깊이가 10인 트리
int x;

//자기 자신(루트노드)를 기준으로 자식노드들을 왼>오 순서로 다음 깊이의 배열(벡터배열사용)에 넣는다
void pushBinaryTree(int currentDepth, int front, int back) {
	
	if (front >= back)
		return;
	
	int mid = (front + back) / 2;

	depth[currentDepth].push_back(input[mid]);
	pushBinaryTree(currentDepth + 1, front, mid);
	pushBinaryTree(currentDepth + 1, mid + 1, back);

	
}


int main() {

	int k; //이진트리 깊이
	cin >> k;
	numberOfNodes = pow(2, k) - 1; // 깊이가 n인 완전이진트리에서의 노드 개수는 n^2 - 1
	x = k;

	for (int i = 0; i < numberOfNodes; i++) {
		cin >> input[i];
	}



		
	pushBinaryTree(0, 0, numberOfNodes);

	for (int i = 0; i < k; i++) { //깊이 지정

		for (int j = 0; j < pow(2, i); j++) { //특정 깊이의 벡터를 모두 출력
			cout << depth[i].at(j) << " ";
		}

		cout << "\n";
	}


	return 0;
}