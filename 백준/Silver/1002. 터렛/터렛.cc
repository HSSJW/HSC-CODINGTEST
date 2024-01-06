#include <iostream>
using namespace std;

int main() {
	int t;
	int x1, y1, r1, x2, y2, r2;
	int dis, rad1, rad2;
	cin >> t;

	for (int i = 0; i < t; i++) {
		cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
		dis = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
		rad1 = (r1 - r2) * (r1 - r2);
		rad2 = (r1 + r2) * (r1 + r2);

		if (dis == 0) {
			if (rad1 == 0)
				cout << "-1" << '\n';
			else
				cout << "0" << '\n';
		}
		else if (dis == rad1 || dis == rad2)
			cout << "1" << '\n';
		else if (rad1 < dis && dis < rad2)
			cout << "2" << '\n';
		else
			cout << "0" << '\n';
	}

	return 0;
}