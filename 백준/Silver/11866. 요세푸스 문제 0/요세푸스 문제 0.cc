#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int main() {
	int n, k, i;
	scanf("%d %d", &n, &k);
	int index = 0, count = 0;
	int a = 0;
	int* narray = (int*)malloc(sizeof(int) * n);
	int* save = (int*)malloc(sizeof(int) * n);
	for (i = 0; i < n; i++) { //모든 칸을 1로 초기화 >> 1이면 사람이 있다는 뜻
		narray[i] = 1;
	}

	for (index = 0; count != n; index) {
		a = 0;
			do {
				
				if (narray[index] == 1) {
					a++;
					index = (index + 1) % n;
				}
				else {
					index = (index + 1) % n;
				}
			} while (a != k);  // 사람이있는 index나올 때까지 다음칸으로
			
			narray[((index - 1) + n)% n] = 0;
			save[count++] = ((index - 1) + n) % n;
			

	}
	
	printf("<");
	for (i = 0; i < n -1; i++) {
		printf("%d, ", (save[i] + 1) % (n+1));
	}
	printf("%d>", (save[n-1] + 1) % (n+1));
	free(narray);
	free(save);
	return 0;
}