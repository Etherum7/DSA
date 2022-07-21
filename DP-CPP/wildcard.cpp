// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
public:
    int wildCard(string pat, string str)
    {
        int n = pat.size();
        int m = str.size();
        // vector<vector<int>> dp(n+1, vector<int>(m+1, 0));
        vector<int> dp(m + 1, 0);
        vector<int> cur(m + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= n; i++)
        {

            int flag = 1;
            for (int ii = 1; ii <= i; ii++)
            {
                if (pat[ii - 1] != '*')
                {
                    flag = 0;
                    break;
                }
            }

            cur[0] = flag;
            for (int j = 1; j <= m; j++)
            {
                if (str[j - 1] == pat[i - 1] || pat[i - 1] == '?')
                {
                    cur[j] = dp[j - 1];
                }
                else if (pat[i - 1] == '*')
                {
                    cur[j] = dp[j] || cur[j - 1];
                }
                else
                    cur[j] = 0;
            }
            dp = cur;
        }
        return dp[m];
    }
    int wildCard(string pat, string str)
    {
        int n = pat.size();
        int m = str.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
        dp[0][0] = 1;
        for (int i = 1; i <= n; i++)
        {
            if (pat[i - 1] == '*' and dp[i - 1][0])
            {
                dp[i][0] = 1;
            }
            for (int j = 1; j <= m; j++)
            {
                if (str[j - 1] == pat[i - 1] or pat[i - 1] == '?')
                {
                    dp[i][j] = dp[i - 1][j - 1];
                }
                else if (pat[i - 1] == '*')
                {
                    dp[i][j] = dp[i - 1][j] || dp[i][j - 1];
                }
            }
        }
        return dp[n][m];
    }
    /*You are required to complete this method*/
    int f(int i, int j, string &pat, string &str, vector<vector<int>> &dp)
    {
        if (i < 0 && j < 0)
        {
            return 1;
        }
        if (i < 0 and j >= 0)
        {
            return 0;
        }
        if (j < 0)
        {
            while (i >= 0)
            {
                if (pat[i] != '*')
                {
                    return 0;
                }
                i -= 1;
            }
            return 1;
        }
        if (dp[i][j] != -1)
            return dp[i][j];
        if (str[j] == pat[i] or pat[i] == '?')
        {
            return dp[i][j] = f(i - 1, j - 1, pat, str, dp);
        }
        else if (pat[i] == '*')
        {
            return dp[i][j] = f(i - 1, j, pat, str, dp) || f(i, j - 1, pat, str, dp);
        }
        else
        {
            return 0;
        }
    }
    int wildCard(string pattern, string str)
    {
        int n = pattern.size();
        int m = str.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, -1));
        return f(n, m, pattern, str, dp);
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string pat, text;
        cin >> pat;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cin >> text;
        Solution obj;
        cout << obj.wildCard(pat, text) << endl;
    }
}
// } Driver Code Ends