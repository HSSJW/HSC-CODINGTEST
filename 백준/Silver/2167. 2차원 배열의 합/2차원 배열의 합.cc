#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int n, m, i, j, k, x, y ;

	int sum, count = 0;
	int list[305][305];

	scanf("%d %d", &n, &m);
	

	for (int i = 1; i <= n; i++)
		for (int k = 1; k <= m; k++)
			scanf("%d", &list[i][k]);

	scanf("%d", &k);

	while (count != k)
	{
		sum = 0;
		scanf("%d %d %d %d", &i, &j, &x, &y);

		for (int p = i; p <= x; p++)
			for (int t = j; t <= y; t++)
				sum += list[p][t];

		printf("%d\n", sum);

		count++;
	}


	return 0;
}