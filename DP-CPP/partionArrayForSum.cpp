class Solution {
public:
 int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int n= arr.size();
        vector<int> dp(n+1, 0);
        for(int i=n-1; i>=0;i--){
            int maxTill=0;
        int ans=0;
        for(int j=i;j<i+k && j<n;j++){
            maxTill= max(maxTill, arr[j]);
            int cost = (j-i+1)*maxTill+ dp[j+1];
            ans= max(ans, cost);
        }
        dp[i]=ans;
        }
        return dp[0];
    }
    int f(int i, int k, int n, vector<int>& arr, vector<int> &dp){
        if(i==n){
            return 0;
        }
        if(dp[i]!=-1) return dp[i];
        int maxTill=0;
        int ans=0;
        for(int j=i;j<i+k && j<n;j++){
            maxTill= max(maxTill, arr[j]);
            int cost = (j-i+1)*maxTill+ f(j+1, k, n, arr, dp);
            ans= max(ans, cost);
        }
        return dp[i]=ans;
    }
    int maxSumAfterPartitioning(vector<int>& arr, int k) {
        int n= arr.size();
        vector<int> dp(n, -1);
        return f(0, k, n, arr, dp);
    }
};