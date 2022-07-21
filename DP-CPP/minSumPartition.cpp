// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{

public:
    vector<bool> subsetSum(int N, int K, int arr[])
    {
        vector<bool> dp(K + 1, false);
        vector<bool> temp(K + 1, false);
        dp[0] = true;

        if (arr[0] < K)
            dp[arr[0]] = true;
        for (int ind = 1; ind < N; ind++)
        {
            for (int target = 1; target <= K; target++)
            {
                temp[target] = dp[target];
                if (target - arr[ind] >= 0)
                {
                    temp[target] = temp[target] | dp[target - arr[ind]];
                }
            }
            dp = temp;
        }
        return dp;
    }
    int minDifference(int arr[], int n)
    {
        // Your code goes here
        int sum = accumulate(arr, arr + n, 0);
        vector<bool> last = subsetSum(n, sum, arr);
        int mini = 1e9;
        // int target=sum/2;
        for (int s1 = 0; s1 <= sum; s1++)
        {
            if (last[s1])
            {

                mini = min(mini, abs((sum - s1) - s1));
            }
        }
        return mini;
    }
};

// { Driver Code Starts.
int main()
{

    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;

        int a[n];
        for (int i = 0; i < n; i++)
            cin >> a[i];

        Solution ob;
        cout << ob.minDifference(a, n) << "\n";
    }
    return 0;
} // } Driver Code Ends