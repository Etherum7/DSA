#include <bits/stdc++.h>
using namespace std;
long countWaysToMakeChange(int *den, int n, int value)
{
    // Write your code her
    //     vector<vector<long>> dp(n, vector<long>(value+1, 0));
    vector<long> dp(value + 1, 0);
    vector<long> cur(value + 1, 0);
    dp[0] = 1;

    for (int tar = 0; tar <= value; tar++)
    {
        if (tar % den[0] == 0)
            dp[tar] = 1;
    }
    for (int ind = 1; ind < n; ind++)
    {
        for (int target = 0; target <= value; target++)
        {
            long notPick = dp[target];
            long pick = 0;
            if (den[ind] <= target)
            {
                pick = cur[target - den[ind]];
            }
            cur[target] = pick + notPick;
        }
        dp = cur;
    }
    return dp[value];
}
long f(int ind, int target, int *den, vector<vector<long>> &dp)
{
    if (target == 0)
    {
        return 1;
    }
    if (ind == 0)
    {
        if (target % den[ind] == 0)
        {
            return 1;
        }
        return 0;
    }
    if (dp[ind][target] != -1)
    {
        return dp[ind][target];
    }
    long notPick = f(ind - 1, target, den, dp);
    long pick = 0;
    if (den[ind] <= target)
    {
        pick = f(ind, target - den[ind], den, dp);
    }
    return dp[ind][target] = pick + notPick;
}
long countWaysToMakeChange(int *den, int n, int value)
{
    // Write your code her
    vector<vector<long>> dp(n, vector<long>(value + 1, 0));
    for (int i = 0; i < n; i++)
    {
        dp[i][0] = 1;
    }
    for (int tar = 0; tar <= value; tar++)
    {
        if (tar % den[0] == 0)
            dp[0][tar] = 1;
    }
    for (int ind = 1; ind < n; ind++)
    {
        for (int target = 1; target <= value; target++)
        {
            long notPick = dp[ind - 1][target];
            long pick = 0;
            if (den[ind] <= target)
            {
                pick = dp[ind][target - den[ind]];
            }
            dp[ind][target] = pick + notPick;
        }
    }
    return dp[n - 1][value];
}