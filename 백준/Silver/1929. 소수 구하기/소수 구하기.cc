#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int save[1000001];


int main() {

	int i;
	int a, b;
	int number = 1000000;
	
	scanf("%d %d", &a, &b);

	for (i = 2; i <= b; i++) {
		save[i] = i;
	}
	for (i = 2; i <= b; i++) {
		if (save[i] == 0)
			continue;
		for (int j = i + i; j <= b; j += i) {
			save[j] = 0;
		}
	}

	for (i = a; i <= b; i++) {
		if (save[i] != 0)
			printf("%d\n", save[i]);
	}


	return 0;

}
