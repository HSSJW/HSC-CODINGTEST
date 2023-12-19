#include <iostream>
using namespace std;

pair<char, char> node[26];
int n;

void preorder(char x) {

	if (x != '.') { // 단말노드가 아닐경우
		cout << x;
		preorder(node[x -'A'].first); //왼쪽 자식노드 탐색
		preorder(node[x - 'A'].second); //오른쪽 자식노드 탐색
	}
}


void inorder(char x) {
	if (x != '.') {
		inorder(node[x - 'A'].first);
		cout << x;
		inorder(node[x - 'A'].second);
	}
}

void postorder(char x) {

	if (x != '.') { // 단말노드가 아닐경우
		
		postorder(node[x - 'A'].first); //왼쪽 자식노드 탐색
		postorder(node[x - 'A'].second); //오른쪽 자식노드 탐색
		cout << x;
	}
}


int main() {

	cin >> n;

	for (int i = 0; i < n; i++) {
		char parent, left, right;
		cin >> parent >> left >> right;

		node[(parent - 'A')].first = left;
		node[(parent)-'A'].second = right;
	}

	preorder('A'); //A가 루트노드
	cout << endl;
	inorder('A');
	cout << endl;
	postorder('A');


	return 0;
}