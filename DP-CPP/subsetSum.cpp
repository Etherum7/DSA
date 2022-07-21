#include <bits/stdc++.h>
using namespace std;

int main()
{

    return 0;
}
class Solution
{
    // Space Optimized
    bool isSubsetSum(vector<int> arr, int sum)
    {
        // code here
        int n = arr.size();
        vector<bool> dp(sum + 1, false);
        dp[0] = true;
        dp[arr[0]] = true;
        vector<bool> temp(sum + 1, false);

        for (int i = 1; i < n; i++)
        {
            for (int target = 0; target <= sum; target++)
            {
                temp[target] = dp[target];
                if (target - arr[i] >= 0)
                {
                    temp[target] = temp[target] | dp[target - arr[i]];
                }
            }
            dp = temp;
        }
        return dp[sum];
    }

public:
    bool isSubsetSum(vector<int> arr, int sum)
    {
        // code here
        int n = arr.size();
        vector<vector<bool>> dp(n, vector<bool>(sum + 1, false));
        for (int i = 0; i < n; i++)
        {
            dp[i][0] = true;
        }
        if (arr[0]<sum) dp[0][arr[0]] = true;
        for (int i = 1; i < n; i++)
        {
            for (int target = 0; target <= sum; target++)
            {
                dp[i][target] = dp[i - 1][target];
                if (target - arr[i] >= 0)
                {
                    dp[i][target] = dp[i][target] | dp[i - 1][target - arr[i]];
                }
            }
        }
        return dp[n - 1][sum];
        // return f(n-1, sum, arr, dp);
    }
    bool f(int ind, int target, vector<int> &arr, vector<vector<int>> &dp)
    {
        if (target == 0)
        {
            return true;
        }
        if (ind == 0)
        {
            return arr[0] == target;
        }
        if (dp[ind][target] != -1)
            return dp[ind][target];

        bool nottake = f(ind - 1, target, arr, dp);
        bool take = false;
        if (target >= arr[ind])
            take = f(ind - 1, target - arr[ind], arr, dp);
        return dp[ind][target] = nottake || take;
    }
    bool isSubsetSum(vector<int> arr, int sum)
    {
        // code here
        int n = arr.size();
        vector<vector<int>> dp(n, vector<int>(sum + 1, -1));
        return f(n - 1, sum, arr, dp);
    }
};
