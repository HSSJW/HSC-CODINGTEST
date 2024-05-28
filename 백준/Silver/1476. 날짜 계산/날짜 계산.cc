#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


int main() {

	int E, S, M, a, b, c;
	int count = 1;
	scanf("%d %d %d", &E, &S, &M);
	a = b = c = 1;

	while (a != E || b != S || c != M) {  // 숫자가 같아지면 stop
		a++, b++, c++;
		if (a > 15)
			a = 1;
		if (b > 28)
			b = 1;
		if (c > 19)
			c = 1;

		count++;

	}

	printf("%d", count);

	return 0;
}
