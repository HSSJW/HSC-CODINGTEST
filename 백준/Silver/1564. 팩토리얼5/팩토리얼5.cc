#include <iostream>
using namespace std;


int main()
{
	long long n;
	long long result;
	

	cin >> n;
	result = 1;

	// 1 2 3 4 5 6 7 8 9
	for (int i = 1; i <= n; i++)
	{
		result *= i;
		if (result % 10 == 0)
		{
			while (result % 10 == 0)
			{
				result /= 10;
			}
		}

		if (result > 100000)
			result %= 1000000000000;
	}


		

		cout.width(5);
		cout.fill('0');

			cout << result % 100000;
			
		
	return 0;
}