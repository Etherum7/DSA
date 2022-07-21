// 1 row

#include <bits/stdc++.h>
using namespace std;

int main()
{
    
    return 0;
}
int knapsack(vector<int> weight, vector<int> value, int n, int maxWeight)
{
    // Write your code here
    vector<int> dp(maxWeight + 1, 0);
    //     vector <int> cur(maxWeight+1, 0);

    for (int i = weight[0]; i <= maxWeight; i++)
    {
        dp[i] = value[0];
    }
    for (int ind = 1; ind < n; ind++)
    {
        for (int w = maxWeight; w >= 0; w--)
        {
            int nottake = 0 + dp[w];
            int take = -1e9;
            if (weight[ind] <= w)
            {
                take = value[ind] + dp[w - weight[ind]];
            }
            dp[w] = max(take, nottake);
        }
    }
    return dp[maxWeight];
    //     return f(n-1, maxWeight, weight, value, dp);
}

int knapsack(vector<int> weight, vector<int> value, int n, int maxWeight)
{
    // Write your code here
    vector<int> dp(maxWeight + 1, 0);
    vector<int> cur(maxWeight + 1, 0);

    for (int i = weight[0]; i <= maxWeight; i++)
    {
        dp[i] = value[0];
    }
    for (int ind = 1; ind < n; ind++)
    {
        for (int w = 1; w <= maxWeight; w++)
        {
            int nottake = 0 + dp[w];
            int take = -1e9;
            if (weight[ind] <= w)
            {
                take = value[ind] + dp[w - weight[ind]];
            }
            cur[w] = max(take, nottake);
        }
        dp = cur;
    }
    return dp[maxWeight];
    //     return f(n-1, maxWeight, weight, value, dp);
}

int f(int ind, int W, vector<int> &weight, vector<int> &value, vector<vector<int>> &dp)
{
    if (ind == 0)
    {
        if (weight[0] <= W)
        {
            return value[0];
        }
        return 0;
    }
    if (dp[ind][W] != -1)
    {
        return dp[ind][W];
    }
    int nottake = 0 + f(ind - 1, W, weight, value, dp);
    int take = -1e9;
    if (weight[ind] <= W)
    {
        take = value[ind] + f(ind - 1, W - weight[ind], weight, value, dp);
    }
    return dp[ind][W] = max(nottake, take);
}