#include <bits/stdc++.h>
using namespace std;

int main()
{

    return 0;
}
class Solution
{
public:
    int knapSack(int N, int W, int val[], int wt[])
    {
        // code here
        vector<vector<int>> dp(N, vector<int>(W + 1, 0));
        for (int w = 0; w <= W; w++)
        {
            dp[0][w] = int(w / wt[0]) * val[0];
        }
        for (int ind = 1; ind < N; ind++)
        {
            for (int w = 0; w <= W; w++)
            {
                int nottake = 0 + dp[ind - 1][w];
                int take = INT_MIN;
                if (w >= wt[ind])
                {
                    take = val[ind] + dp[ind][w - wt[ind]];
                }
                dp[ind][w] = max(nottake, take);
            }
        }
        return dp[N - 1][W];
    }
    int f(int ind, int W, int *val, int *wt, vector<vector<int>> &dp)
    {
        if (ind == 0)
        {
            return int(W / wt[0]) * val[0];
        }
        if (dp[ind][W] != -1)
        {
            return dp[ind][W];
        }
        int nottake = 0 + f(ind - 1, W, val, wt, dp);
        int take = 0;
        if (W >= wt[ind])
        {
            take = val[ind] + f(ind, W - wt[ind], val, wt, dp);
        }
        return dp[ind][W] = max(nottake, take);
    }
    int knapSack(int N, int W, int val[], int wt[])
    {
        // code here
        vector<vector<int>> dp(N, vector<int>(W + 1, -1));
        return f(N - 1, W, val, wt, dp);
    }
};

int knapSack(int N, int W, int val[], int wt[])
{
    // code here
    // vector<vector<int>> dp (N, vector<int>(W+1, 0));
    vector<int> dp(W + 1, 0);
    // vector<int> cur(W+1, 0);
    for (int w = 0; w <= W; w++)
    {
        dp[w] = int(w / wt[0]) * val[0];
    }
    for (int ind = 1; ind < N; ind++)
    {
        for (int w = 0; w <= W; w++)
        {
            int nottake = 0 + dp[w];
            int take = INT_MIN;
            if (w >= wt[ind])
            {
                take = val[ind] + dp[w - wt[ind]];
            }
            dp[w] = max(nottake, take);
        }
        // dp=cur;
    }
    return dp[W];
}