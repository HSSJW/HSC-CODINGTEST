#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
    int n, temp;
    int i, j, t, k;
    int sumi = 0, sumj = 0;
    char serial[50][51];
    char cpy[51];
    int len[50];
    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        scanf("%s", serial[i]);
    }

    for (i = 0; i < n; i++) {
        len[i] = strlen(serial[i]);
    }

    for (i = 0; i < n; i++) {
        for (j = i + 1; j < n; j++) {  // i+1부터 시작하여 중복 정렬 방지
            if (len[i] > len[j]) {  // 1번 조건
                temp = len[i];
                len[i] = len[j];
                len[j] = temp;

                strcpy(cpy, serial[i]);
                strcpy(serial[i], serial[j]);
                strcpy(serial[j], cpy);
            }
            else if (len[i] == len[j]) {
                sumi = 0, sumj = 0;  // 초기화
                for (t = 0; t < len[i]; t++) {
                    if (serial[i][t] >= '0' && serial[i][t] <= '9') { // 숫자인지 확인하는 조건문 수정
                        sumi += serial[i][t] - '0';  // 숫자의 합 계산
                    }
                }

                for (t = 0; t < len[j]; t++) {
                    if (serial[j][t] >= '0' && serial[j][t] <= '9') { // 숫자인지 확인하는 조건문 수정
                        sumj += serial[j][t] - '0';  // 숫자의 합 계산
                    }
                }

                if (sumi != sumj) {  // 2번 조건
                    if (sumi > sumj) {
                        strcpy(cpy, serial[i]);
                        strcpy(serial[i], serial[j]);
                        strcpy(serial[j], cpy);
                    }
                }
                else {  // 3번 조건
                    if (strcmp(serial[i], serial[j]) > 0) {
                        strcpy(cpy, serial[i]);
                        strcpy(serial[i], serial[j]);
                        strcpy(serial[j], cpy);
                    }
                }
            }
        }
    }

    for (i = 0; i < n; i++) {
        printf("%s\n", serial[i]);
    }

    return 0;
}