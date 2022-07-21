#include <bits/stdc++.h>
using namespace std;

int main()
{

    return 0;
}
class Solution
{
public:
    // Function to find the length of longest common subsequence in two strings.
    int lcs(int x, int y, string s1, string s2)
    {
        // your code here
        int n = s1.size();
        int m = s2.size();
        // vector<vector<int>> dp(n+1, vector<int>(m + 1, 0));
        vector<int> dp(m + 1, 0);
        vector<int> cur(m + 1, 0);
        for (int ind1 = 1; ind1 <= n; ind1++)
        {
            for (int ind2 = 1; ind2 <= m; ind2++)
            {
                if (s1[ind1 - 1] == s2[ind2 - 1])
                {
                    cur[ind2] = 1 + dp[ind2 - 1];
                }
                else
                {
                    cur[ind2] = max(dp[ind2], cur[ind2 - 1]);
                }
            }
            dp = cur;
        }
        return dp[m];
    }

    int f(int ind1, int ind2, string s1, string s2, vector<vector<int>> &dp)
    {
        if (ind1 < 0 || ind2 < 0)
            return 0;
        if (dp[ind1][ind2] != -1)
        {
            return dp[ind1][ind2];
        }
        if (s1[ind1] == s2[ind2])
        {
            return dp[ind1][ind2] = 1 + f(ind1 - 1, ind2 - 1, s1, s2, dp);
        }
        else
        {
            return dp[ind1][ind2] = max(f(ind1 - 1, ind2, s1, s2, dp), f(ind1, ind2 - 1, s1, s2, dp));
        }
    }
    // Function to find the length of longest common subsequence in two strings.
    int lcs(int x, int y, string s1, string s2)
    {
        // your code here
        int n = s1.size();
        int m = s2.size();
        vector<vector<int>> dp(n + 1, vector<int>(m + 1, -1));
        return f(n - 1, m - 1, s1, s2, dp);
    }
};