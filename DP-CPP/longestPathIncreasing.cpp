//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
public:
    bool isSafe(int i, int j, int n, int m)
    {
        return i >= 0 and i < n and j >= 0 and j < m;
    }
    int f(int i, int j, int n, int m, vector<vector<int>> &matrix, vector<vector<int>> &dp)
    {
        if (dp[i][j] != -1)
            return dp[i][j];
        int dx[] = {1, 0, -1, 0};
        int dy[] = {0, 1, 0, -1};
        int ans = 1;
        for (int k = 0; k < 4; k++)
        {
            int newX = i + dx[k];
            int newY = j + dy[k];
            if (isSafe(newX, newY, n, m) and matrix[newX][newY] > matrix[i][j])
            {
                ans = max(ans, 1 + f(newX, newY, n, m, matrix, dp));
            }
        }
        return dp[i][j] = ans;
    }
    int longestIncreasingPath(vector<vector<int>> &matrix)
    {
        // Code here

        int n = matrix.size();
        int m = matrix[0].size();
        int res = 0;
        vector<vector<int>> dp(n, vector<int>(m, -1));
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                res = max(res, f(i, j, n, m, matrix, dp));
            }
        }
        return res;
    }
};

//{ Driver Code Starts.
int main()
{
    int tc;
    cin >> tc;
    while (tc--)
    {
        int n, m;
        cin >> n >> m;
        vector<vector<int>> matrix(n, vector<int>(m, 0));
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                cin >> matrix[i][j];
        Solution obj;
        int ans = obj.longestIncreasingPath(matrix);
        cout << ans << "\n";
    }
    return 0;
}
// } Driver Code Ends