// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{

public:
    int f(int ind, int target, int *coins, vector<vector<int>> &dp)
    {

        if (ind == 0)
        {
            if (target % coins[ind] == 0)
            {
                return target / coins[ind];
            }
            return 1e9;
        }
        if (dp[ind][target] != -1)
            return dp[ind][target];
        int notpick = 0 + f(ind - 1, target, coins, dp);
        int pick = INT_MAX;
        if (target >= coins[ind])
        {
            pick = 1 + f(ind, target - coins[ind], coins, dp);
        }
        return dp[ind][target] = min(pick, notpick);
    }
    int minCoins(int arr[], int M, int V)
    {
        // Your code goes here
        // vector<vector<int>> dp(M, vector<int>(V+1, 0));
        vector<int> dp(V + 1, 0);
        vector<int> cur(V + 1, 0);
        for (int tar = 0; tar <= V; tar++)
        {
            if (tar % arr[0] == 0)
                dp[tar] = tar / arr[0];
            else
                dp[tar] = 1e9;
        }
        for (int ind = 1; ind < M; ind++)
        {
            for (int target = 0; target <= V; target++)
            {
                int notpick = 0 + dp[target];
                int pick = INT_MAX;
                if (target >= arr[ind])
                {
                    pick = 1 + cur[target - arr[ind]];
                }
                cur[target] = min(pick, notpick);
            }
            dp = cur;
        }
        int ans = dp[V];

        if (ans >= 1e9)
            return -1;
        return ans;
    }
};

// { Driver Code Starts.
int main()
{

    int t;
    cin >> t;
    while (t--)
    {
        int v, m;
        cin >> v >> m;

        int coins[m];
        for (int i = 0; i < m; i++)
            cin >> coins[i];

        Solution ob;
        cout << ob.minCoins(coins, m, v) << "\n";
    }
    return 0;
}
// } Driver Code Ends
int minCoins(int arr[], int M, int V)
{
    // Your code goes here
    vector<vector<int>> dp(M, vector<int>(V + 1, 1e9));
    for (int tar = 0; tar <= V; tar++)
    {
        if (tar % arr[0] == 0)
            dp[0][arr[0]] = tar / arr[0];
        else
            dp[0][arr[0]] = 1e9;
    }
    for (int ind = 1; ind < M - 1; ind++)
    {
        for (int target = 0; target <= V; target++)
        {
            int notpick = 0 + dp[ind - 1][target];
            int pick = INT_MAX;
            if (target >= arr[ind])
            {
                pick = 1 + dp[ind][target - arr[ind]];
            }
            dp[ind][target] = min(pick, notpick);
        }
    }
    int ans = dp[M - 1][V];

    if (ans >= 1e9)
        return -1;
    return ans;
}

// } Driver Code Ends
class Solution
{

public:
    int f(int ind, int target, int coins[], vector<vector<int>> &dp)
    {

        if (ind == 0)
        {
            if (target % coins[ind] == 0)
            {
                return target / coins[ind];
            }
            return 1e9;
        }
        if (dp[ind][target] != -1)
            return dp[ind][target];
        int notpick = 0 + f(ind - 1, target, coins, dp);
        int pick = INT_MAX;
        if (target >= coins[ind])
        {
            pick = 1 + f(ind, target - coins[ind], coins, dp);
        }
        return dp[ind][target] = min(pick, notpick);
    }
    int minCoins(int coins[], int M, int V)
    {
        // Your code goes here
        vector<vector<int>> dp(M, vector<int>(V + 1, -1));
        int ans = f(M - 1, V, coins, dp);

        if (ans >= 1e9)
            return -1;
        return ans;
    }
};

// { Driver Code Starts.
int main()
{

    int t;
    cin >> t;
    while (t--)
    {
        int v, m;
        cin >> v >> m;

        int coins[m];
        for (int i = 0; i < m; i++)
            cin >> coins[i];

        Solution ob;
        cout << ob.minCoins(coins, m, v) << "\n";
    }
    return 0;
}
// } Driver Code Ends