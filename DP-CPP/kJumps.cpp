#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int kjumps(int n, int k, vector<int> &heights)
{
    if (n == 0)
    {
        return 0;
    }
    vector<int> dp(n, 0);

    for (int i = 1; i < n; i++)
    {
        int minSteps = INT_MAX;
        for (int j = 1; j <= k; j++)
        {
            if ((i - j) >= 0)
            {
                int jumpEnergy = dp[i - j] + abs(heights[i] - heights[i - j]);
                minSteps = min(minSteps, jumpEnergy);
            }
            dp[i] = minSteps;
        }
    }
    return dp[n - 1];
}
int main()
{
    int arr[] = {30, 10, 60, 10, 60, 50};
    int n = sizeof(arr) / sizeof(arr[0]);
    vector<int> heights(arr, arr+n);
    cout<<arr+n<<endl;
    
    cout << kjumps(6, 3, heights) << endl;
    return 0;
}