#include <iostream>
using namespace std;

int* min_list(int* Array, int n)
{
	int i, j;
	int temp;

	for(i = 0; i < n; i++)
		for (j = 0; j < n; j++)
		{
			if (Array[i] > Array[j])
			{
				temp = Array[i];
				Array[i] = Array[j];
				Array[j] = temp;
			}
		}
	return Array;
}

int* max_list(int* Array, int n)
{
	int i, j;
	int temp;

	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++)
		{
			if (Array[i] < Array[j])
			{
				temp = Array[i];
				Array[i] = Array[j];
				Array[j] = temp;
			}
		}
	return Array;
}

int main()
{

	int n;
	int sum = 0;
	cin >> n;
	int* A = new int[n];
	int* B = new int[n];

	for (int i = 0; i < n; i++)
	{
		cin >> A[i];
	}

	for (int i = 0; i < n; i++)
	{
		cin >> B[i];
	}

	A = max_list(A, n);
	B = min_list(B, n);

	for (int i = 0; i < n; i++)
	{
		sum += A[i] * B[i];
	}

	cout << sum;

	return 0;
}