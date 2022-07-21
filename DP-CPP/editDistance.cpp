// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
public:
    int editDistance(string s, string t)
    {
        // Code here
        int n = s.size();
        int m = t.size();
        vector<int> dp(m + 1, 0);
        vector<int> cur(m+1 , 0);

        for (int i = 0; i <= m; i++)
        {
            dp[i] = i;
        }

        // dp[0][0]=0;
        for (int i = 1; i <= n; i++)
        {
            cur[0] = i;
            for (int j = 1; j <= m; j++)
            {
                if (s[i - 1] == t[j - 1])
                {
                    cur[j] = dp[j - 1];
                }
                else
                {
                    int replace = 1 + dp[j - 1];
                    int del = 1 + dp[j];
                    int insert = 1 + cur[j - 1];
                    cur[j] = min(replace, min(del, insert));
                }
            }
            dp = cur;
        }
        return dp[m];
    }
    int editDistance(string s, string t)
    {
        // Code here
        int n = s.size();
        int m = t.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
        for (int i = 0; i <= n; i++)
        {
            dp[i][0] = i;
        }
        for (int j = 0; j <= m; j++)
        {
            dp[0][j] = j;
        }
        // dp[0][0]=0;
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= m; j++)
            {
                if (s[i - 1] == t[j - 1])
                {
                    dp[i][j] = dp[i - 1][j - 1];
                }
                else
                {
                    int replace = 1 + dp[i - 1][j - 1];
                    int del = 1 + dp[i - 1][j];
                    int insert = 1 + dp[i][j - 1];
                    dp[i][j] = min(replace, min(del, insert));
                }
            }
        }
        return dp[n][m];
    }
    int f(int i, int j, string &s, string &t, vector<vector<int>> &dp)
    {
        if (i < 0)
        {
            return j + 1;
        }
        if (j < 0)
        {
            return i + 1;
        }
        if (dp[i][j] != -1)
        {
            return dp[i][j];
        }
        if (s[i] == t[j])
        {
            return dp[i][j] = f(i - 1, j - 1, s, t, dp);
        }
        else
        {
            int replace = 1 + f(i - 1, j - 1, s, t, dp);
            int del = 1 + f(i - 1, j, s, t, dp);
            int insert = 1 + f(i, j - 1, s, t, dp);
            return dp[i][j] = min(replace, min(del, insert));
        }
    }
    int editDistance(string s, string t)
    {
        // Code here
        int n = s.size();
        int m = t.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, -1));
        return f(n - 1, m - 1, s, t, dp);
    }
};

// { Driver Code Starts.
int main()
{
    int T;
    cin >> T;
    while (T--)
    {
        string s, t;
        cin >> s >> t;
        Solution ob;
        int ans = ob.editDistance(s, t);
        cout << ans << "\n";
    }
    return 0;
}
// } Driver Code Ends