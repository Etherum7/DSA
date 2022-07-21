// { Driver Code Starts
//Initial Template for C++

#include<bits/stdc++.h>
using namespace std;

int removals(vector<int>& a, int k){
        //Code here
        sort(a.begin(), a.end());
        int n= a.size();
        vector<int> ahead(n+1, 0);
        vector<int> cur(n+1, 0);
        for(int i=n-1; i>=0;i--){
            for(int j=i;j<n;j++ ){
                if(a[j]-a[i]<k){
                 cur[j]= 0;
                 continue;
                }
                else{
                cur[j]= 1+min(ahead[ j],cur[ j-1]);
                }
            }
            ahead=cur;
        }
        return ahead[n-1];
    }
 // } Driver Code Ends
//User function Template for C++
 int removals(vector<int>& a, int k){
        //Code here
        sort(a.begin(), a.end());
        int n= a.size();
        vector<vector<int>> dp(n+1, vector<int>(n+1, 0));
        for(int i=n-1; i>=0;i--){
            for(int j=i;j<n;j++ ){
                if(a[j]-a[i]<k){
                 dp[i][j]= 0;
                 continue;
                }
                else{
                dp[i][j]= 1+min(dp[i+1][ j],dp[i][ j-1]);
                }
            }
        }
        return dp[0][n-1];
    }

class Solution{
    public:
    int f(int i, int j, vector<int>& a, int k, vector<vector<int>> &dp){
        if(i>j){
            return 0;
        }
        if(dp[i][j]!=-1) return dp[i][j];
        if(a[j]-a[i]<k){
            return dp[i][j]= 0;
        }
        else{
            return dp[i][j]= 1+min(f(i+1, j, a, k, dp), f(i, j-1, a, k, dp));
        }
        
    }
    int removals(vector<int>& a, int k){
        //Code here
        sort(a.begin(), a.end());
        int n= a.size();
        vector<vector<int>> dp(n, vector<int>(n, -1));
        return f(0, n-1, a, k, dp);
    }
        
};


// { Driver Code Starts.


int main(){
    int t;
    cin>>t;
    
    while(t--){
        int n,k;
        cin>>n>>k;
        vector<int> a(n);
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
        
        Solution ob;
        int ans = ob.removals(a,k);
        
        cout<<ans<<endl;
    }
}


  // } Driver Code Ends
class Solution
{
public:
    int removals(vector<int> &a, int k)
    {
        // Code here
        sort(a.begin(), a.end());
        int i = 0;
        int n = a.size();
        int j = 0;
        int cnt = INT_MAX;
        int diff = 0;
        while (j < n)
        {
            diff = a[j] - a[i];
            while (i <= j and diff >= k)
            {
                diff -= a[i];
                i += 1;
            }
            cnt = min(cnt, (n - (j - i + 1)));
            j += 1;
        }
        return cnt;
    }
};