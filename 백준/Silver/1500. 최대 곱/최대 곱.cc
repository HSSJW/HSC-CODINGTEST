#include <iostream>
using namespace std;

long long S, K, ans = 1;
long long tmp1, tmp2;

int main() 
{
    cin >> S >> K;

    tmp1 = S / K;
    tmp2 = S % K;

    for (int i = 0; i < K; i++)
    {
        if (tmp2 > 0)
        {
            ans *= (tmp1 + 1);
            tmp2--;
        }
        else ans *= tmp1;
    }
    cout << ans;
}