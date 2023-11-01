#include <iostream>
using namespace std;



int main() {
    int n, m;
    int count = 0;
    int start = 0, end = 0;
    cin >> n >> m;

    int *a = new int[n+1];

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    
    int result = a[0];

    while (start <= end && end < n) {
        if (result < m) {
            result += a[++end];
        }
        else if (result == m) {
            count++;
            result += a[++end];
        }
        else if (result > m) {
            result -= a[start++];

            if (start > end) {
                end = start;
                result = a[start];
            }
        }
    }

    cout << count;
}