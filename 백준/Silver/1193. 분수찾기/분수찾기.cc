#include <iostream>
using namespace std;

//짝왼 홀오

int main()
{

	int input;
	int i, j;
	int count = 0;
	int sum = 0;

	cin >> input;

	for (i = 1;; i++)
	{
		sum += i;
		if (sum >= input)
			break;
	}
	// i가 탐색해야하는 줄 번호로 나온다

	j = input - sum + i - 1;  // 해당줄 탐색개수
	int k = 1;

	if (i % 2 == 1) // 홀수

	{
		for (j; j > 0; j--)
		{
			i--;
			k++;
		}
		cout << i << '/' << k;
	}
	else
	{
		for (j; j > 0; j--)
		{
			i--;
			k++;
		}
		cout << k << '/' << i;
	}


	return 0;
}