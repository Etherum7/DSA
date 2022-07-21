#include <bits/stdc++.h>
using namespace std;

int main()
{
    
    return 0;
}
int subsetSum(int N, int K, int arr[])
{
    vector<vector<bool>> dp(N, vector<bool>(K + 1, false));
    for (int i = 0; i < N; i++)
    {
        dp[i][0] = true;
    }
    dp[0][arr[0]] = true;
    for (int ind = 1; ind < N; ind++)
    {
        for (int target = 1; target <= K; target++)
        {
            dp[ind][target] = dp[ind - 1][target];
            if (target - arr[ind] >= 0)
            {
                dp[ind][target] = dp[ind][target] | dp[ind - 1][target - arr[ind]];
            }
        }
    }
    return dp[N - 1][K];
}
int equalPartition(int N, int arr[])
{
    // code here

    int sum = accumulate(arr, arr + N, 0);
    // int sum=10;
    if ((sum % 2) != 0)
    {
        return false;
    }
    return subsetSum(N - 1, sum / 2, arr);
}