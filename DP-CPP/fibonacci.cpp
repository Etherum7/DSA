#include <bits/stdc++.h>
using namespace std;
int fib(int n, vector<int> &dp)
{
    if (n <= 1)
    {
        return n;
    }
    if (dp[n] != -1)
    {
        return dp[n];
    }
    return dp[n] = fib(n - 1, dp) + fib(n - 2, dp);
}

int fib2Tabulation(int n)
{
    int prev2 = 0;
    int prev1 = 1;
    

    for (int i = 2; i <= n; i++)
    {
        int curi = prev2 + prev1;
        prev2 = prev1;
        prev1 = curi;
    }
    return prev1;
}

int main()
{
    int n;
    cin >> n;
    vector<int> dp(n + 1, -1);
    // memset(dp, -1, sizeof(dp))
    // cout << fib(n, dp) << endl;
    cout << fib2Tabulation(n) << endl;
    return 0;
}