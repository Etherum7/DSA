int longestCommonSubstr(string s1, string s2, int n, int m)
{
    // your code here
    int maxTill = 0;

    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    for (int ind1 = 1; ind1 <= n; ind1++)
    {
        for (int ind2 = 1; ind2 <= m; ind2++)
        {
            if (s1[ind1 - 1] == s2[ind2 - 1])
            {
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1];
                maxTill = max(maxTill, dp[ind1][ind2]);
            }
            else
            {
                dp[ind1][ind2] = 0;
            }
        }
    }
    return maxTill;
}

;
#include <bits/stdc++.h>
using namespace std;

int main()
{

    return 0;
}