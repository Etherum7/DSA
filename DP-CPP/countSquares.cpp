int countSquares(int n, int m, vector<vector<int>> &arr)
{
    // Write your code here.
    vector<vector<int>> dp(n, vector<int>(m, 0));
    int squares = 0;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (i == 0 or j == 0)
            {
                dp[i][j] = arr[i][j];
                squares += arr[i][j];
                continue;
            }
            if (arr[i][j] == 0)
            {
                dp[i][j] = 0;
                //                 continue;
            }
            else
            {
                dp[i][j] = min(dp[i - 1][j], min(dp[i - 1][j - 1], dp[i][j - 1])) + 1;
                squares += dp[i][j];
            }
        }
    }
    return squares;
}
