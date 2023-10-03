#include <iostream>

int main() {
    int zero[41]={1,0,};
    int one[41]={0,1,};
    int T,n;

    scanf("%d",&T);
    for (int i=0; i<T; i++) {
        scanf("%d",&n);
        for (int j = 2 ; j<=n; j++) {
            zero[j] = zero[j-1] +zero[j-2];
            one[j] = one[j-1] + one[j-2];
        }
        printf("%d %d\n",zero[n],one[n]);
    }

}