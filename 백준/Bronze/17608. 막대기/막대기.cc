#include <iostream>
#include <vector>
using namespace std;



int main() {

	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	cin >> n;

	int* tall = new int[n];
	int count = 1;  //첫번째 기둥은 보이는 것으로 상정
	
	int second = 0;

	for (int i = 0; i < n; i++) {
		cin >> tall[i];
	}

	int max = tall[n - 1]; //첫번째(오른쪽) 기둥의 높이

	for (int i = n - 1; i >= 0; i--) {
		if (max < tall[i]) {
			count++;
			max = tall[i];
		}
	}

	cout << count;



	return 0;
}