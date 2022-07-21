#include <bits/stdc++.h>
using namespace std;

int main()
{
    
    return 0;
}
class Solution
{
public:
    vector<int> largestDivisibleSubset(vector<int> &nums)
    {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        // vector<int>

        vector<int> dp(n, 1);
        vector<int> hash(n, 0);
        int maxi = 1;
        int lastIndex = 0;
        for (int i = 0; i < n; i++)
        {
            hash[i] = i;
            for (int j = 0; j < i; j++)
            {
                if (nums[i] % nums[j] == 0 && dp[i] < 1 + dp[j])
                {
                    dp[i] = 1 + dp[j];
                    hash[i] = j;
                }
            }
            if (maxi < dp[i])
            {
                maxi = dp[i];
                lastIndex = i;
            }
        }
        vector<int> res;
        res.push_back(nums[lastIndex]);
        while (lastIndex != hash[lastIndex])
        {
            lastIndex = hash[lastIndex];
            res.push_back(nums[lastIndex]);
        }
        reverse(res.begin(), res.end());
        return res;
    }
};