//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
public:
    int f(int i, int j, string &str1, string &str2)
    {
        if (i < 0 || j < 0)
        {
            return 0;
        }
        if (str1[i] == str2[j] && i != j)
        {
            return 1 + f(i - 1, j - 1, str1, str2);
        }
        else
        {
            return max(f(i - 1, j, str1, str2), f(i, j - 1, str1, str2));
        }
    }
    int LongestRepeatingSubsequence(string str)
    {
        // Code here
        int n = str.size();
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
        for (int i = 1; i < n + 1; i++)
        {
            for (int j = 1; j < n + 1; j++)
            {
                if (str[i - 1] == str[j - 1] && i - 1 != j - 1)
                {
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                }
                else
                {
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[n][n];
    }
};

//{ Driver Code Starts.
int main()
{
    int tc;
    cin >> tc;
    while (tc--)
    {
        string str;
        cin >> str;
        Solution obj;
        int ans = obj.LongestRepeatingSubsequence(str);
        cout << ans << "\n";
    }
    return 0;
}
// } Driver Code Ends