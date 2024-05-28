#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
    int n;

    cin >> n;

    int arr[1001];
    int dp[1001];

    for (int i = 0; i < n; i++)
        cin >> arr[i];

    
    for (int i = 0; i < n; i++)
        dp[i] = 1;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j <= i; j++)      
            if (arr[i] > arr[j])
                dp[i] = max(dp[i], dp[j] + 1);
            
    }

    sort(dp, dp + n);

    cout << dp[n - 1];
}