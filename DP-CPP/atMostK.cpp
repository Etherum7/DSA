#include <bits/stdc++.h>
using namespace std;

int main()
{

    return 0;
}
int maxProfit(int K, int N, int arr[])
{
    // code here
    //  int n = A.size();

    vector<int> dp(2 * K + 1, 0);
    vector<int> cur(2 * K + 1, 0);
    for (int ind = N - 1; ind >= 0; ind--)
    {
        for (int transNo = (2 * K) - 1; transNo >= 0; transNo--)
        {
            if (transNo % 2 == 0)
            {
                cur[transNo] = max(-arr[ind] + dp[transNo + 1],
                                   dp[transNo]);
            }
            else
            {
                cur[transNo] = max(arr[ind] + dp[transNo + 1],
                                   dp[transNo]);
            }
        }
        dp = cur;
    }
    return dp[0];
}
int maxProfit(int K, int N, int arr[])
{
    // code here
    //  int n = A.size();

    vector<vector<int>> dp(N + 1, vector<int>(2 * K + 1, 0));
    for (int ind = N - 1; ind >= 0; ind--)
    {
        for (int transNo = (2 * K) - 1; transNo >= 0; transNo--)
        {
            if (transNo % 2 == 0)
            {
                dp[ind][transNo] = max(-arr[ind] + dp[ind + 1][transNo + 1],
                                       dp[ind + 1][transNo]);
            }
            else
            {
                dp[ind][transNo] = max(arr[ind] + dp[ind + 1][transNo + 1],
                                       dp[ind + 1][transNo]);
            }
        }
    }
    return dp[0][0];
}
int f(int ind, int transNo, int K, int n, int *arr, vector<vector<int>> &dp)
{
    if (transNo == 2 * K or ind == n)
    {
        return 0;
    }
    if (dp[ind][transNo] != -1)
        return dp[ind][transNo];
    if (transNo % 2 == 0)
    {
        return dp[ind][transNo] = max(-arr[ind] + f(ind + 1, transNo + 1, K, n, arr, dp),
                                      f(ind + 1, transNo, K, n, arr, dp));
    }
    else
    {
        return dp[ind][transNo] = max(arr[ind] + f(ind + 1, transNo + 1, K, n, arr, dp),
                                      f(ind + 1, transNo, K, n, arr, dp));
    }
}
int maxProfit(int K, int N, int arr[])
{
    // code here
    //  int n = A.size();

    vector<vector<int>> dp(N + 1, vector<int>(2 * K, -1));
    return f(0, 0, K, N, arr, dp);
}
int maxProfit(int K, int N, int arr[])
{
    // code here
    //  int n = A.size();

    vector<vector<vector<int>>> dp(N + 1, vector<vector<int>>(K + 1, vector<int>(2, 0)));
    for (int i = N - 1; i >= 0; i--)
    {
        for (int cap = 1; cap <= K; cap++)
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
    }
    return dp[0][K][1];
}