   int longestSubsequence(int n, int a[])
    {
        // vector < vector < int >> dp(n+1, vector < int > (n+1, 0));
        vector < int > dp(n, 1);
        vector < int > hash(n, 1);
        int maxTill = 1;
        // vector < int > cur(n+1, 0);
        for(int ind=0; ind < n; ind++){
            hash[ind] = ind;
            for(int prev_ind=0; prev_ind < ind; prev_ind++){
                if (a[prev_ind] < a[ind]){
                    if(1+dp[prev_ind] > dp[ind]){
                        dp[ind] = 1+dp[prev_ind];
                        hash[ind] = prev_ind;
                        maxTill = max(maxTill, dp[ind]);}
                }

            }
            cout<<hash[ind]<<" ";}
       // your code here
       return maxTill; }
};
