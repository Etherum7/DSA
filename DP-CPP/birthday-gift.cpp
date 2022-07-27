#include <bits/stdc++.h>
using namespace std;

int main()
{

    return 0;
}
#define MOD 10000
int dfs(int i, int k, int n, vector<vector<int>> &dp)
{
    if (k == 0)
    {
        return 1;
    }
    if (dp[i][k] != -1)
        return dp[i][k];
    int res = 0;
    for (int l = i; l <= n; l++)
    {

        if (l % i == 0)
        {
            res = (res % MOD + dfs(l, k - 1, n, dp) % MOD) % MOD;
        }
    }
    return dp[i][k] = res;
}
int findways(int n, int k)
{
    int ans = 0;
    vector<vector<int>> dp(n, vector<int>(k, -1));
    for (int i = 1; i <= n; i++)
    {
        ans = (ans % MOD + dfs(i, k - 1, n, dp) % MOD) % MOD;
    }
    return ans;
}