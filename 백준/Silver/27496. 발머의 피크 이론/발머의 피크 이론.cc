#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, l;
	cin >> n >> l;
	long long sum = 0;
	int count = 0;

	vector<int> v(n + 1);
	v[0] = 0;

	for (int i = 1; i < n+1; i++) {
		cin >> v[i];
		v[i] = v[i - 1] + v[i];

	}
	
	for (int i = 1; i < l; i++) {
		if (129 <= v[i] && v[i] <= 138)
			count++;
	}


	for (int i = l; i < n + 1; i++) {

		sum = v[i] - v[i - l];

		if (129 <= sum && sum <= 138) {
			count++;
		}
	}
	
	cout << count;


	return 0;
}