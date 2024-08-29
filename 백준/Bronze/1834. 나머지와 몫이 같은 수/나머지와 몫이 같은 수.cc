#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>


int main()
{
	long long x, result = 0, n = 1, sum = 0;

	scanf("%lld", &x);

	

	while (n < pow(x, 2))
	{
		if (n / x == n % x) {
			result = n;
			break;
		}
		n++;
	}


	int count = pow(x, 2) / result;

	for (long long i = 1; i <= count; i++)
		sum += result * i;
	
	
	printf("%lld", sum);

	return 0;
}