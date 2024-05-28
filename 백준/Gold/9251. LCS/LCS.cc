#include <iostream>
#include <algorithm>
using namespace std;
int arr[1005][1005];

int main() {

	string a, b;
	

	cin >> a;
	cin >> b;

	for (int i = 0; i <= a.length(); i++) {
		arr[0][i] = 0;

	}

	for (int i = 0; i <= b.length(); i++) {
		arr[i][0] = 0;
	}

	for(int i = 1; i <= a.length(); i++)
		for (int j = 1; j <= b.length(); j++) {

			if (a[i-1] == b[j-1]) { // 최소 공통수열에 알맞은 일치하는 문자가 있는 경우
				arr[i][j] = arr[i - 1][j - 1] + 1;
			}
			else { //일치하지 않는걍우
				arr[i][j] = max(arr[i - 1][j], arr[i][j - 1]);
			}
		}


	cout << arr[a.size()][b.size()];

	return 0;
}