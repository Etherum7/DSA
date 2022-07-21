
class Solution{
    public:
    //Function to count subarrays with sum equal to 0.
    ll findSubarray(vector<ll> arr, int n ) {
        //code here
        map<int, int> mp;
        mp[0]=1;
        int cur=0;
        int res=0;
        for(int i=0; i<n;i++){
            
            cur+=arr[i];
            if(mp.find(cur)!=mp.end()){
                res+=mp[cur];
                // cout<<cur<<' '<<mp[cur]<<' ';
            }
            mp[cur]+=1;
        }
        return res;
    }
};