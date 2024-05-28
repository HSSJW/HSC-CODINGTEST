#include <iostream>
using namespace std;



int main()
{
	int array[101][101] = { 0 };

	int x, y, k = 4;
	int a, b, c, d;
	int count = 0;

	while (k--)
	{
		cin >> a >> b >> c >> d;

		for (x = a; x < c; x++)
			for (y = b; y < d; y++)
			{
				if (array[x][y] != 1)
				{
					count++;
					array[x][y] = 1;
				}
				}
	}


	cout << count;

	return 0;
}