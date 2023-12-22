#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{

	int man, a, b, round = 0;

	scanf("%d %d %d", &man, &a, &b);

	
	while (a != b)
	{

		a = a - a/2;           // 승리시 a의 다음 번호
		b = b - b/2;		   // 승리시 b의 다음 번호
		round++;
		
	}

	printf("%d", round);



	return 0;
}