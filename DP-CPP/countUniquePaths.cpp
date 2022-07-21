#include <bits/stdc++.h>
using namespace std;

int main()
{

    return 0;
}

// Space Optimized
long long int numberOfPaths(int m, int n)
{
    // code here
    // vector<vector<long long int>> dp(m, vector<long long int>(n, -1));
    vector<long long int> dp(n, 0);
    vector<long long int> temp(n, 0);

    // dp[0][0]=1;
    for (int i = 0; i < m; i++)
    {

        for (int j = 0; j < n; j++)
        {
            if (i == 0 && j == 0)
            {
                temp[j] = 1;
            }
            else
            {
                int up = 0;
                int left = 0;

                if (i > 0)
                    up = dp[j];
                if (j > 0)
                    left = temp[j - 1];
                temp[j] = (up + left) % 1000000007;
            }
        }
        dp = temp;
    }
    return dp[n - 1];
}
// Tabulation
long long int numberOfPaths(int m, int n)
{
    // code here
    vector<vector<long long int>> dp(m, vector<long long int>(n, -1));
    // dp[0][0]=1;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == 0 && j == 0)
            {
                dp[0][0] = 1;
            }
            else
            {
                int up = 0;
                int left = 0;
                if (i > 0)
                    up = dp[i - 1][j];
                if (j > 0)
                    left = dp[i][j - 1];
                dp[i][j] = (up + left) % 1000000007;
            }
        }
    }
    return dp[m - 1][n - 1];
}
class Solution
{
public:
    long long int f(int i, int j, vector<vector<long long int>> &dp)
    {
        if (i == 0 && j == 0)
        {
            return 1;
        }
        if (i < 0 || j < 0)
        {
            return 0;
        }
        if (dp[i][j] != -1)
        {
            return dp[i][j];
        }
        long long int up = f(i - 1, j, dp);
        long long int left = f(i, j - 1, dp);
        dp[i][j] = (up + left) % 1000000007;
        return dp[i][j];
    }
    long long int numberOfPaths(int m, int n)
    {
        // code here
        vector<vector<long long int>> dp(m, vector<long long int>(n, -1));
        return f(m - 1, n - 1, dp);
    }
};