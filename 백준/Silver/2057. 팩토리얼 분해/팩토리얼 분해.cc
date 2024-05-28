#include <iostream>
using namespace std;
typedef long long ll;

ll fact[20];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	fact[0] = 1;
	for (ll i = 1; i < 20; i++) {
		fact[i] = fact[i - 1] * i;
	}

	ll N; cin >> N;

	if (N == 0) cout << "NO";
	else {
		for (int i = 19; i > -1; i--) {
			if (N >= fact[i]) N -= fact[i];
		}
		if (N) cout << "NO";
		else cout << "YES";
	}
}