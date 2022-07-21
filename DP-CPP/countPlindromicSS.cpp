// { Driver Code Starts
// Counts Palindromic Subsequence in a given String
#include<bits/stdc++.h>
using namespace std;

 // } Driver Code Ends
class Solution{
    public:
    int mod=1000000007;
    /*You are required to complete below method */
    long long int f(int i, int j, string &str, vector<vector<long long int>> &dp){
        if(i>j){
            return 0;
        }
        if(i==j){
            return 1;
        }
        if(dp[i][j]!=-1) return dp[i][j];
        if(str[i]==str[j]){
            return dp[i][j]=(1+f(i+1,j, str, dp)%mod+f(i, j-1, str, dp)%mod+mod)%mod;
            // return 1+f(i+1, j-1)+f(i+1,j)+f(i, j-1)-f(i+1, j-1);
        }
        else{
            return dp[i][j]=(f(i+1,j, str, dp)%mod+f(i, j-1, str, dp)%mod-f(i+1,j-1, str, dp)%mod+mod)%mod;
        }
    }
    long long int  countPS(string str)
    {
       //Your code here
       int n= str.size();
       vector<vector<long long int>> dp(n, vector<long long int>(n, -1));
       return f(0, n-1, str, dp);
       
    }
     
};

// { Driver Code Starts.
// Driver program
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        string str;
        cin>>str;
        Solution ob;
        long long int ans = ob.countPS(str);
        cout<<ans<<endl;
    } 
}  // } Driver Code Ends