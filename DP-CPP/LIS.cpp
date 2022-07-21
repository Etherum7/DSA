// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends

class Solution
{
public:
int longestSubsequence(int n, int a[])
    {
        // vector<vector<int>> dp(n+1, vector<int>(n+1, 0));
        vector<int> dp(n, 1);
        int maxTill=1;
        // vector<int> cur(n+1, 0);
        for(int ind=0; ind<n;ind++){
            for(int prev_ind=0;prev_ind<ind;prev_ind++){
                if (a[prev_ind]<a[ind]){
                    dp[ind]= max(1+dp[prev_ind], dp[ind]);
                    maxTill=max(maxTill, dp[ind]);
                }
               
            }
            
        }
       // your code here
       return maxTill;
    }
    int longestSubsequence(int n, int a[])
    {
        // vector<vector<int>> dp(n+1, vector<int>(n+1, 0));
        vector<int> dp(n + 1, 0);
        vector<int> cur(n + 1, 0);
        for (int ind = n - 1; ind >= 0; ind--)
        {
            for (int prev_ind = ind - 1; prev_ind >= -1; prev_ind--)
            {
                int len1 = 0 + dp[prev_ind + 1];
                int len2 = 0;
                if (prev_ind == -1 or a[prev_ind] < a[ind])
                {
                    len2 = 1 + dp[ind + 1];
                }
                cur[prev_ind + 1] = max(len1, len2);
            }
            dp = cur;
        }
        // your code here
        return dp[0];
    }
    int longestSubsequence(int n, int a[])
    {
        vector<vector<int>> dp(n + 1, vector<int>(n + 1, 0));
        for (int ind = n - 1; ind >= 0; ind--)
        {
            for (int prev_ind = ind - 1; prev_ind >= -1; prev_ind--)
            {
                int len1 = 0 + dp[ind + 1][prev_ind + 1];
                int len2 = 0;
                if (prev_ind == -1 or a[prev_ind] < a[ind])
                {
                    len2 = 1 + dp[ind + 1][ind + 1];
                }
                dp[ind][prev_ind + 1] = max(len1, len2);
            }
        }
        // your code here
        return dp[0][0];
    }
    int f(int ind, int prev_ind, int *a, int n, vector<vector<int>> &dp)
    {
        if (ind == n)
        {
            return 0;
        }
        if (dp[ind][prev_ind + 1] != -1)
            return dp[ind][prev_ind + 1];
        int len1 = 0 + f(ind + 1, prev_ind, a, n, dp);
        int len2 = 0;
        if (prev_ind == -1 or a[prev_ind] < a[ind])
        {
            len2 = 1 + f(ind + 1, ind, a, n, dp);
        }
        return dp[ind][prev_ind + 1] = max(len1, len2);
    }

    // Function to find length of longest increasing subsequence.
    int longestSubsequence(int n, int a[])
    {
        vector<vector<int>> dp(n, vector<int>(n + 1, -1));
        // your code here
        return f(0, -1, a, n, dp);
    }
};

// { Driver Code Starts.
int main()
{
    // taking total testcases
    int t, n;
    cin >> t;
    while (t--)
    {
        // taking size of array
        cin >> n;
        int a[n];

        // inserting elements to the array
        for (int i = 0; i < n; i++)
            cin >> a[i];
        Solution ob;
        // calling method longestSubsequence()
        cout << ob.longestSubsequence(n, a) << endl;
    }
}
// } Driver Code Ends