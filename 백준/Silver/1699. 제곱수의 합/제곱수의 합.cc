#include <iostream>
using namespace std;

// 그리드 >> 가장 큰수의 경우부터 제거하면서 탐색하는 방식
//F[n]이란  n을 가장 최소개수의 제곱수합으로 더해서 구할 수있는 수

int d[100000];
int main()
{
	int n;
	cin >> n;


	for (int i = 1; i <= n; i++)
	{
		d[i] = i;  //일단 1^2*n으로 표현해두기 

		for (int j = 1; j * j <= i; j++)
		{
			if (d[i] > d[i - j * j] + 1)  // 자신보다 작은 제곱수들로 표현가능한 최소개수
				d[i] = d[i - j * j] + 1;
		}
	}

	cout << d[n];

	return 0;
}