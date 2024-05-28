#include <iostream>
#include <algorithm>
using namespace std;



int main()
{
	int n;

	cin >> n;
	int* num = new int[n];

	for (int i = 0; i < n; i++)
	{
		cin >> num[i];
	}

	int count = 0;

	sort(num, num + n);

	cout << num[0] * num[n - 1];

	return 0;
}