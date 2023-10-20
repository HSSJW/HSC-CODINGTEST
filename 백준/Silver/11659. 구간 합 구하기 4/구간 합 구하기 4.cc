#include <iostream>
using namespace std;


int main() {

	int n, m, i, j;
	int k;
	cin >> n >> m;

	int *num = new int[n+1];

	num[0] = 0;

	for (k = 1; k <= n; k++) {   //숫자 순서 저장
		cin >> num[k];
		num[k] = num[k - 1] + num[k];  //배열[현재인덱스] = 배열[이전 인덱스] + 현재인덱스

	}

	for (k = 0; k < m; k++) {
		scanf("%d %d", &i, &j);

		printf("%d\n", num[j] - num[i - 1]);
	}
	
	return 0;
}