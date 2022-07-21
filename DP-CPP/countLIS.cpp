class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int n= nums.size();
	    vector<int> dp(n, 1);
	    vector<int> cnt(n, 1);
        // int cnt=1;
        int maxi=1;
	    
	    for(int i=1 ; i<n; i++){
	        for(int j=0; j<i;j++){
	            if(nums[j]<nums[i] and dp[i]<1+dp[j]){
	                dp[i]=1+dp[j];
                    cnt[i]=cnt[j];}
                else if(dp[i]==1+dp[j]){
                        cnt[i]+=cnt[j];
                    }
	                
	            }
            maxi=max(maxi, dp[i]);
	        }
        
            
	    
        int res=0;
    
	    for(int i=0; i<n;i++){
            if (dp[i]==maxi){
                res+=cnt[i];
            }
        }
        return res;
        
    }
};