#include <bits/stdc++.h>
using namespace std;

int main()
{
    
    return 0;
}
int mod = (int)(1e9 + 7);
int f(int ind, int target, vector<int> &arr, vector<vector<int>> &dp)
{

    if (ind == 0)
    {
        if (target == 0 && arr[0] == 0)
        {
            return 2;
        }
        if (target == 0 || arr[ind] == target)
        {
            return 1;
        }
        return 0;
    }

    if (dp[ind][target] != -1)
    {
        return dp[ind][target];
    }
    int nottake = f(ind - 1, target, arr, dp);
    int take = 0;
    if (arr[ind] <= target)
    {
        take += f(ind - 1, target - arr[ind], arr, dp);
    }
    return dp[ind][target] = (nottake + take) % mod;
}

int countPartitions(int n, int d, vector<int> &arr)
{
    // Write your code here.

    int sum = 0;
    for (auto &it : arr)
    {
        sum += it;
    }
    if (sum < d || (sum - d) % 2)
    {
        return 0;
    }
    //     cout<<sum<<endl;

    int K = (sum - d) / 2;

    vector<vector<int>> dp(n, vector<int>(K + 1, 0));

    if (arr[0] == 0)
        dp[0][0] = 2;
    else
        dp[0][0] = 1;

    if (arr[0] != 0 && arr[0] <= K)
        dp[0][arr[0]] = 1;

    for (int ind = 1; ind < n; ind++)
    {
        for (int target = 0; target <= K; target++)
        {
            int nottake = dp[ind - 1][target];
            int take = 0;
            if (arr[ind] <= target)
            {
                take += dp[ind - 1][target - arr[ind]];
            }
            dp[ind][target] = (take + nottake) % mod;
        }
    }
    return dp[n - 1][K];
}
