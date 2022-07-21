#include <bits/stdc++.h>
using namespace std;

int main()
{
    
    return 0;
}

int minimumPathSum(vector<vector<int>>& triangle, int n){
	// Write your code here.
    vector<vector<int>>dp(n, vector<int>(n,-1));
    for (int j=0; j<n;j++){
        dp[n-1][j]=triangle[n-1][j];
    }
    for(int i=n-2; i>=0;i--){
        for(int j=0;j<i+1;j++){
            int down = triangle[i][j]+dp[i+1][j];
            int dig= triangle[i][j]+dp[i+1][ j+1];
            dp[i][j]=min(down, dig);
            
        }
    }
//     return f(0,0,n, triangle, dp);
    return dp[0][0];
}
int f(int i, int j, int n, vector<vector<int>> &triangle, vector<vector<int>> &dp)
{
    if (i == n - 1)
    {
        return triangle[i][j];
    }
    int down = triangle[i][j] + f(i + 1, j, n, triangle, dp);
    int dig = triangle[i][j] + f(i + 1, j + 1, n, triangle, dp);
    dp[i][j] = min(down, dig);
    return dp[i][j];
}
int minimumPathSum(vector<vector<int>> &triangle, int n)
{
    // Write your code here.
    vector<vector<int>> dp(n, vector<int>(n, -1));
    return f(0, 0, n, triangle, dp);
}