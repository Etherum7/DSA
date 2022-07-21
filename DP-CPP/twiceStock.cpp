// Write your code here..
int maxProfit(vector<int> &arr)
{
    // Write your code here..
    int n = arr.size();

    // vector<vector<vector<int>>>dp(n+1,vector<vector<int>>(3,vector<int>(2,0)));
    vector<vector<int>> dp(3, vector<int>(2, 0));
    vector<vector<int>> curr(3, vector<int>(2, 0));
    for (int i = n - 1; i >= 0; i--)
    {
        for (int cap = 1; cap <= 2; cap++)
        {
            for (int buy = 1; buy >= 0; buy--)
            {
                if (buy)
                {
                    curr[cap][buy] = max(-arr[i] + dp[cap][0], dp[cap][1]);
                }
                else
                    curr[cap][buy] = max(arr[i] + dp[cap - 1][1], dp[cap][0]);
            }
        }
        dp = curr;
        // cout<<i<<dp[i][2][1]<<" ";
    }
    return dp[2][1];
}
int maxProfit(vector<int> &arr)
{
    int n = arr.size();

    vector<vector<vector<int>>> dp(n + 1, vector<vector<int>>(3, vector<int>(2, 0)));
    for (int i = n - 1; i >= 0; i--)
    {
        for (int cap = 1; cap <= 2; cap++)
        {
            for (int buy = 1; buy >= 0; buy--)
            {
                if (buy)
                {
                    dp[i][cap][buy] = max(-arr[i] + dp[i + 1][cap][0], dp[i + 1][cap][1]);
                }
                else
                    dp[i][cap][buy] = max(arr[i] + dp[i + 1][cap - 1][1], dp[i + 1][cap][0]);
            }
        }
        // cout<<i<<dp[i][2][1]<<" ";
    }
    return dp[0][2][1];
}

int fun(vector<int> &arr, int i, int b, int k, vector<vector<vector<int>>> &dp)
{
    if (k == 0 or i == arr.size())
        return 0;
    if (dp[i][k][b] != -1)
        return dp[i][k][b];
    if (b)
        return dp[i][k][b] = max(-arr[i] + fun(arr, i + 1, 0, k, dp), fun(arr, i + 1, 1, k, dp));
    else
        return dp[i][k][b] = max(arr[i] + fun(arr, i + 1, 1, k - 1, dp), fun(arr, i + 1, 0, k, dp));
}

int maxProfit(vector<int> &arr)
{
    // Write your code here..
    int n = arr.size();
    int k = 2;
    int b = 1;
    vector<vector<vector<int>>> dp(n + 1, vector<vector<int>>(k + 1, vector<int>(b + 1, -1)));
    return fun(arr, 0, b, k, dp);
}

#include <bits/stdc++.h>
using namespace std;

int main()
{

    return 0;
}