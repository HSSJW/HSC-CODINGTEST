#include <iostream>
using namespace std;


int  main() {

	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);


	string l, r;
	int res = 0;


	cin >> l >> r;

	if (l.length() != r.length()) {
		cout << res;
		return 0;
	}


	for (int i = 0; i < l.length(); i++) {
		if (l[i] == r[i] && l[i] == '8') {
			res++;
		}
		else if (l[i] != r[i])
		{
			break;
		}
	}

	cout << res;
	return 0;
}