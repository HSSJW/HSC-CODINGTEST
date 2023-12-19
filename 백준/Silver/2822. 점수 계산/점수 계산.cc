#include <iostream>
using namespace std;


int main() {


	int n[2][8];
	int temp = NULL;
	int sum = 0;


	for (int i = 0; i < 8; i++) {
		cin >> n[0][i]; //1열 >> 점수
		n[1][i] = i+1; // 2열 >> 각 점수가 들어있는 순서 1~8
	}

	for(int i = 0; i < 8; i++)
		for (int j = 0; j < 8; j++) {
			if (n[0][i] < n[0][j]) {
				temp = n[0][i];		//점수 교환
				n[0][i] = n[0][j];
				n[0][j] = temp;

				temp = n[1][i];   //점수 순서 교환
				n[1][i] = n[1][j];
				n[1][j] = temp;
			}

			
		}
	//정렬 완료


	for (int i = 3; i < 8; i++) {
		sum += n[0][i];
	}

	cout << sum << "\n";

	for (int i = 3; i < 8; i++)
		for (int j = 3; j < 8; j++) {
			if (n[1][i] < n[1][j]) {
				temp = n[1][i];
				n[1][i] = n[1][j];
				n[1][j] = temp;

			}

		}
	for (int i = 3; i < 8; i++)
		cout << n[1][i] << " ";

	return 0;
}