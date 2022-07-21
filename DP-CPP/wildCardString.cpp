// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function template for C++
class Solution
{
public:
    int f(int i, int j, string wild, string pattern, vector<vector<int>> &dp)
    {
        if (i < 0 and j < 0)
        {
            return 1;
        }

        if (j < 0)
        {
            while (i >= 0)
            {
                if (wild[i] != '*')
                {
                    return 0;
                }
                i -= 1;
            }
            return 1;
        }
        if (i < 0)
        {
            return 0;
        }
        if (dp[i][j] != -1)
            return dp[i][j];
        if (wild[i] == pattern[j] or wild[i] == '?')
        {
            return dp[i][j] = f(i - 1, j - 1, wild, pattern, dp);
        }
        else if (wild[i] == '*')
        {
            return dp[i][j] = f(i - 1, j, wild, pattern, dp) or f(i, j - 1, wild, pattern, dp);
        }
        return dp[i][j] = 0;
    }
    bool match(string wild, string pattern)
    {
        // code here
        int n = wild.size();
        int m = pattern.size();
        vector<vector<int>> dp(n, vector<int>(m, -1));
        return f(n - 1, m - 1, wild, pattern, dp);
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string wild, pattern;
        cin >> wild >> pattern;

        Solution ob;
        if (ob.match(wild, pattern))
            cout << "Yes\n";
        else
            cout << "No\n";
    }
    return 0;
} // } Driver Code Ends