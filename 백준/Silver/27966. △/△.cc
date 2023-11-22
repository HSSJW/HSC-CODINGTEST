#include <iostream>
using namespace std;



int main() {

	long long n;
	cin >> n;


	cout << n-1 + (n-1) * (n-2) << "\n";

	for (long long k = 2; k <= n; k++) {
		cout << "1 " << k << "\n";
	}

	return 0;
}