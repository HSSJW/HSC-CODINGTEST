#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
	
	int n; //삼각형의 높이
	int dp[500][500];
	cin >> n;

	
	for (int i = 0; i < n; i++) {
		
		for (int j = 0; j <= i; j++) { //해당 층의 원소개수는 층+1
			
			cin >> dp[i][j]; //일단 해당칸에 입력한후 뒤에서 다시 더해서 저장
		}

	}

	for (int i = 1; i < n; i++) {
		for (int j = 0; j <= i; j++) {

			if (j == 0)
				dp[i][j] += dp[i - 1][j]; //위층 첫번째 칸
			else if (j == i)
				dp[i][j] += dp[i - 1][j - 1];
			else
				dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j]);


		}
	}

	int max = 0;

	for (int i = 0; i < n; i++) {
		
		if (max < dp[n - 1][i])
			max = dp[n - 1][i];
	}

	cout << max;

	return 0;
}