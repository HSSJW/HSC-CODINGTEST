#include <iostream>
using namespace std;

int arr[1025][1025];
int save[1025][1025];

int main() {

	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int n, t;

	cin >> n >> t;



	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			cin >> arr[i][j];  //행렬 입력받기
			save[i][j] = arr[i][j]; //행렬의 원래 값 저장
		}
	}

	for (int i = 0; i <= n; i++) { 
		arr[i][0] = 0;
		arr[0][i] = 0;
	}
	




	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			
			arr[i][j] = arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1] + save[i][j];
			// 합     =  윗열까지합   +  왼쪽행까지의합  -   겹치는부분
		}
	}

	int a, b, c, d;
	int result = 0;
	

	for (int i = 0; i < t; i++) {
		cin >> a >> b >> c >> d;
		
		result = arr[c][d] - arr[c][b - 1] - arr[a - 1][d] + arr[a - 1][b - 1];

	  
		cout << result << "\n";

	}



	return 0;

}