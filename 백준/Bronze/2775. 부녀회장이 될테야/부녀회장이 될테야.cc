#include <iostream>
using namespace std;


int main() {


	int t;
	int k, n;
	cin >> t;

	

	for (int i = 0; i < t; i++) {

		cin >> k >> n;
		int** arr = new int*[k+1]; //층수 동적배열

		for (int p = 0; p < k+1; p++) { // 호수 동적배열
			arr[p] = new int[n+1];
		}

		for (int j = 1; j < n+1; j++) { //0층 호수별 인원 초기화
			arr[0][j] = j;
		}

		

		for (int j = 1; j < k+1; j++) { //층수
			int sum = 0;
			for (int p = 1; p < n+1; p++) { //호수
				sum += arr[j - 1][p]; //아래층 1호~b호 사람 합
				arr[j][p] = sum;
			}
			
		}



		cout << arr[k][n] << "\n";
	}


	

	return 0;
}