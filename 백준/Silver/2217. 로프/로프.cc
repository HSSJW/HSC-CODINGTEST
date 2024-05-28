#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b)  // return 1 >> 순서바꿈 >> a가 b보다 크다  // -1 >> Pass  >> b가 더 크다
{
	if (*(int*)a < *(int*)b)  //  (int*) >> a 에저장된 정수값을 '주소'값으로 가져와라 //  *(int*) >> 받아온 주소값을 참조하여 변수값을 가져와라
		return 1;							//    앞에있는 수가 더 크면 1을 반환하여  qsort함수로 자리변환
	else if (*(int*)a >= *(int*)b)
		return -1;

}


int main() {
	
	int i, input;
	int n_loap;
	int* loap_weight;
	scanf("%d", &n_loap);
	loap_weight = (int*)malloc(sizeof(int) * n_loap);

	for (i = 0; i < n_loap; i++) {
		scanf("%d", &loap_weight[i]);
	}

	qsort(loap_weight, n_loap, sizeof(int), compare); // 내림챃순으로 정렬 >> 가장 큰수부터 사용하기 위함

	int result = loap_weight[0]; // 가능한 무게

	for (i = 1; i < n_loap; i++) {
		if (result <= loap_weight[i] * (i + 1)) {
			result = loap_weight[i] * (i + 1);
		}
	}

	printf("%d", result);

	return 0;
}