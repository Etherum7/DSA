int mod = (int)1e9 + 7;
class Solution
{
public:
    int findTargetSumWays(vector<int> &arr, int d)
    {
        // Write your code here.
        int n = arr.size();

        int sum = 0;
        for (auto &it : arr)
        {
            sum += it;
        }
        if (sum < d || (sum - d) % 2)
        {
            return 0;
        }
        //     cout<<sum<<endl;

        int K = (sum - d) / 2;

        vector<vector<int>> dp(n, vector<int>(K + 1, 0));

        if (arr[0] == 0)
            dp[0][0] = 2;
        else
            dp[0][0] = 1;

        if (arr[0] != 0 && arr[0] <= K)
            dp[0][arr[0]] = 1;

        for (int ind = 1; ind < n; ind++)
        {
            for (int target = 0; target <= K; target++)
            {
                int nottake = dp[ind - 1][target];
                int take = 0;
                if (arr[ind] <= target)
                {
                    take += dp[ind - 1][target - arr[ind]];
                }
                dp[ind][target] = (take + nottake) % mod;
            }
        }
        return dp[n - 1][K];
    }
};