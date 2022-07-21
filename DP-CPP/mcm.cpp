#include <bits/stdc++.h>
using namespace std;

int main()
{
    
    return 0;
}
class Solution
{
public:
    int f(int i, int j, int *arr, vector<vector<int>> &dp)
    {
        if (i == j)
        {
            return 0;
        }
        if (dp[i][j] != -1)
            return dp[i][j];
        int mini = INT_MAX;
        for (int k = i; k < j; k++)
        {
            mini = min(mini, f(i, k, arr, dp) + arr[i - 1] * arr[k] * arr[j] + f(k + 1, j, arr, dp));
        }
        return dp[i][j] = mini;
    }
    int matrixMultiplication(int N, int arr[])
    {
        // code here
        vector<vector<int>> dp(N, vector<int>(N, 0));
        for (int i = N - 1; i >= 1; i--)
        {
            for (int j = i + 1; j < N; j++)
            {
                int mini = INT_MAX;
                for (int k = i; k < j; k++)
                {
                    mini = min(mini, dp[i][k] + arr[i - 1] * arr[k] * arr[j] + dp[k + 1][j]);
                }
                dp[i][j] = mini;
            }
        }
        return dp[1][N - 1];
    }
};