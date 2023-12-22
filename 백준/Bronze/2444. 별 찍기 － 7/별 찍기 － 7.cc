#include<iostream>
using namespace std;


int main() {

	int n;
	cin >> n;


	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n - i - 1; j++) //앞에 빈칸
			cout << " ";

		for (int j = 0; j < 1 + 2 * i; j++)
			cout << "*";

		cout << "\n";
	}

	for (int i = n - 2; i >= 0; i--) {

		for (int j = 0; j < n - i - 1; j++) //앞에 빈칸
			cout << " ";

		for (int j = 0; j < 1 + 2 * i; j++)
			cout << "*";

		
		cout << "\n";
	}


	return 0;
}