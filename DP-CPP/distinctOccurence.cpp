// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
/*You are required to complete this method*/

class Solution
{
public:
    int mod = 1000000007;
    int subsequenceCount(string S, string T)
    {
        // Your code here
        int n = S.size();
        int m = T.size();
        //   vector<vector<int>> dp(n+1, vector<int>(m+1 , 0));
        vector<int> dp(m + 1, 0);
        //   vector<int> cur( m+1 , 0);
        dp[0] = 1;
        //   cur[0]=1;

        for (int i = 1; i <= n; i++)
        {
            for (int j = m; j >= 0; j--)
            {
                if (i < j)
                {
                    dp[j] = 0;
                }
                if (S[i - 1] == T[j - 1])
                {
                    dp[j] = (dp[j - 1] % mod + dp[j] % mod) % mod;
                }
                // else
                // {
                //     dp[j] = dp[j] % mod;
                // }
            }
        }
        return dp[m];
    }
};
int subsequenceCount(string S, string T)
{
    // Your code here
    int n = S.size();
    int m = T.size();
    //   vector<vector<int>> dp(n+1, vector<int>(m+1 , 0));
    vector<int> dp(m + 1, 0);
    vector<int> cur(m + 1, 0);
    dp[0] = 1;
    cur[0] = 1;

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            if (S[i - 1] == T[j - 1])
            {
                cur[j] = (dp[j - 1] % mod + dp[j] % mod) % mod;
            }
            else
            {
                cur[j] = dp[j] % mod;
            }
        }
        dp = cur;
    }
    return dp[m];
}
long long f(int i, int j, string &S, string &T, vector<vector<long long>> &dp)
{
    if (j < 0)
    {
        return 1;
    }
    if (i < 0)
    {
        return 0;
    }
    if (dp[i][j] != -1)
        return dp[i][j];
    if (S[i] == S[j])
    {
        return dp[i][j] = (f(i - 1, j - 1, S, T, dp) % mod + f(i - 1, j, S, T, dp) % mod) % mod;
    }
    else
    {
        return dp[i][j] = f(i - 1, j, S, T, dp) % mod;
    }
}
int subsequenceCount(string S, string T)
{
    // Your code here
    int n = S.size();
    int m = T.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    for (int i = 0; i <= n; i++)
    {
        dp[i][0] = 1;
    }
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= m; j++)
        {
            if (S[i - 1] == T[j - 1])
            {
                dp[i][j] = (dp[i - 1][j - 1] % mod + dp[i - 1][j] % mod) % mod;
            }
            else
            {
                dp[i][j] = dp[i - 1][j] % mod;
            }
        }
    }
    return dp[n][m];
}
}
;

// { Driver Code Starts.

//  Driver code to check above method
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string s;
        string tt;
        cin >> s;
        cin >> tt;

        Solution ob;
        cout << ob.subsequenceCount(s, tt) << endl;
    }

} // } Driver Code Ends