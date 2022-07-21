class Solution
{
public:
    int palindromicPartition(string str)
    {
        int n = str.size();
        vector<int> dp(n + 1, 0);
        for (int i = n - 1; i >= 0; i--)
        {
            int mini = INT_MAX;
            for (int j = i; j < n; j++)
            {
                if (isPalindrome(i, j, str))
                {
                    int cost = 1 + dp[j + 1];
                    mini = min(mini, cost);
                }
                dp[i] = mini;
            }
        }
        // for last partion
        return dp[0] - 1;
    }
    int isPalindrome(int i, int j, string str)
    {
        while (i <= j)
        {
            if (str[i] != str[j])
                return 0;
            i++;
            j--;
        }
        return 1;
    }
    int f(int i, int j, string &str, vector<vector<int>> &dp)
    {
        // cout<<i<<' '<<j<<' ';
        if (i > j)
        {
            return 0;
        }
        if (i == j)
        {
            return 0;
        }
        if (dp[i][j] != -1)
            return dp[i][j];
        if (isPalindrome(i, j, str))
            return 0;
        int mini = INT_MAX;
        for (int ind = i + 1; ind <= j; ind++)
        {
            // cout<<i<<' '<<ind-1<<' '<<mini<<' ';
            mini = min(mini, f(i, ind - 1, str, dp) + 1 + f(ind, j, str, dp));
        }
        return dp[i][j] = mini;
    }
    int palindromicPartition(string str)
    {
        // code here
        int n = str.size();
        vector<vector<int>> dp(n, vector<int>(n, -1));
        return f(0, n - 1, str, dp);
    }
};

// { Driver Code Starts
// Initial Template for c++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function Template for C++

class Solution
{
public:
    int isPalindrome(int i, int j, string str)
    {
        // int i=0;
        // int j= str.size();
        while (i <= j)
        {
            if (str[i] != str[j])
                return 0;
            i++;
            j--;
        }
        return 1;
    }
    int f(int i, int n, string &str, vector<int> &dp)
    {
        // cout<<i<<' '<<j<<' ';

        if (i == n)
        {
            return 0;
        }
        if (dp[i] != -1)
            return dp[i];
        // string temp="";

        int mini = INT_MAX;
        for (int j = i; j < n; j++)
        {

            // temp+=str[ind];
            if (isPalindrome(i, j, str))
            {
                int cost = 1 + f(j + 1, n, str, dp);
                mini = min(mini, cost);
            }
        }
        return dp[i] = mini;
    }
    int palindromicPartition(string str)
    {
        int n = str.size();
        vector<int> dp(n + 1, -1);

        // for last partion
        return f(0, n, str, dp) - 1;
    }
};

// { Driver Code Starts.

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string str;
        cin >> str;

        Solution ob;
        cout << ob.palindromicPartition(str) << "\n";
    }
    return 0;
} // } Driver Code Ends