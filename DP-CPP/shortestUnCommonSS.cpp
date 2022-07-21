// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

int shortestUnSub(string S, string T) {
        // code here
        int n= S.size();
        int m =T.size();
        vector<vector<int>> dp(n+1, vector<int>(m+1, 1000));
        for(int i=1;i<=n;i++){
            for(int j=1;j<=m;j++){
                int k=j;
                while(k && S[i-1]!=T[k-1]){
                    k-=1;
                }
                if(k==0){
                    dp[i][j]=1;
                }
                else{
                    dp[i][j]=min(dp[i-1][j], 1+dp[i-1][k-1]);
                }
            }
        }
        // int val= f(0,0, S, T, n,m, dp);
        return  dp[n][m]==1000? -1 : dp[n][m];
        
    }

// } Driver Code Ends
class Solution
{
public:
    int f(int i, int j, string S, string T, int n, int m, vector<vector<int>> &dp)
    {
        if (i == n)
        {
            return 1e9;
        }
        if (j == m)
        {
            return 1;
        }
        if (dp[i][j] != -1)
            return dp[i][j];
        int k = j;
        for (k = j; k < m; k++)
        {
            if (T[k] == S[i])
            {
                break;
            }
        }
        if (k == m)
        {
            return 1;
        }

        int include = 1 + f(i + 1, k + 1, S, T, n, m, dp);
        int exclude = f(i + 1, j, S, T, n, m, dp);
        return dp[i][j] = min(include, exclude);
    }
    int shortestUnSub(string S, string T)
    {
        // code here
        int n = S.size();
        int m = T.size();
        vector<vector<int>> dp(n, vector<int>(m, -1));

        int val = f(0, 0, S, T, n, m, dp);
        return (val >= 1e9) ? -1 : val;
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string S, T;
        cin >> S >> T;

        Solution ob;
        cout << ob.shortestUnSub(S, T) << endl;
    }
    return 0;
} // } Driver Code Ends