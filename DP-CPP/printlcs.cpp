#include <bits/stdc++.h>
using namespace std;

string lcs(string s1, string s2)
{
    // your code here
    int n = s1.size();
    int m = s2.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));
    for (int ind1 = 1; ind1 <= n; ind1++)
    {
        for (int ind2 = 1; ind2 <= m; ind2++)
        {
            if (s1[ind1-1] == s2[ind2-1])
            {
                dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1];
            }
            else
            {
                dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1]);
            }
        }
    }
    int l = dp[n][m];
    int i = n;
    int j = m;
    string s = "";
    for (int i = 0; i < l; i++)
    {
        s += '$';
    }
    int index = l - 1;
    while (i > 0 && j > 0)
    {
        if (s1[i-1] == s2[j-1])
        {
            s[index] = s1[i-1];
            index -= 1;
            i -= 1;
            j -= 1;
        }
        else if (dp[i - 1][j] > dp[i][j - 1])
        {
            i = i - 1;
        }
        else
        {
            j = j - 1;
        }
    }
    cout << s << endl;
    
    return s;
}
int main()
{
    lcs("abcde", "bdgek");
    return 0;
}
