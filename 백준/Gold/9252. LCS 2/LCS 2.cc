#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
int arr[1005][1005];

int main() {

	string a, b;
	int count = 0;
	char save[1005];

	cin >> a;
	cin >> b;

	for (int i = 0; i <= a.length(); i++) {
		arr[0][i] = 0;

	}

	for (int i = 0; i <= b.length(); i++) {
		arr[i][0] = 0;
	}

	for (int i = 1; i <= a.length(); i++)
		for (int j = 1; j <= b.length(); j++) {

			if (a[i - 1] == b[j - 1]) { // 최소 공통수열에 알맞은 일치하는 문자가 있는 경우
				arr[i][j] = arr[i - 1][j - 1] + 1;
			}
			else { //일치하지 않는걍우
				arr[i][j] = max(arr[i - 1][j], arr[i][j - 1]);
			}
		}

	int k = arr[a.size()][b.size()];
	int aIndex = a.size();
	int bIndex = b.size();


	while (true) {

		if (k == 0)
			break;

		if (k == arr[aIndex - 1][bIndex]) { //윗칸이 같으면 윗칸으로 한칸 이동
			k = arr[aIndex - 1][bIndex];
			aIndex = aIndex - 1;
		}
		
		else if (k == arr[aIndex][bIndex - 1]) {
			k = arr[aIndex][bIndex - 1];
			bIndex = bIndex - 1;
		}
		

		else { //같은 숫자 x
			k = arr[aIndex - 1][bIndex - 1];
			save[count] = b[bIndex - 1];
			count++;
			aIndex = aIndex - 1;
			bIndex = bIndex - 1;
			
		}

	}

	

	cout << arr[a.size()][b.size()] << "\n";
	
	for (int i = count - 1; i >= 0; i--) {
		cout << save[i];
	}

	return 0;
}