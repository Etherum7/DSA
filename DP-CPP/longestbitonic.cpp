// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
public:
    int LongestBitonicSequence(vector<int> nums)
    {
        // code here
        int n = nums.size();
        vector<int> dp1(n, 1);
        vector<int> dp2(n, 1);

        for (int i = 1; i < n; i++)
        {
            for (int j = 0; j < i; j++)
            {
                if (nums[j] < nums[i] and dp1[i] < 1 + dp1[j])
                {
                    dp1[i] = 1 + dp1[j];
                }
            }
        }

        for (int i = n - 2; i >= 0; i--)
        {
            for (int j = n - 1; j > i; j--)
            {
                if (nums[j] < nums[i] and dp2[i] < 1 + dp2[j])
                {
                    dp2[i] = 1 + dp2[j];
                }
            }
        }
        int maxTill = 0;
        for (int i = 0; i < n; i++)
        {
            maxTill = max(maxTill, dp1[i] + dp2[i] - 1);
        }
        return maxTill;
    }
};

// { Driver Code Starts.
int main()
{
    int tc;
    cin >> tc;
    while (tc--)
    {
        int n;
        cin >> n;
        vector<int> nums(n);
        for (int i = 0; i < n; i++)
            cin >> nums[i];
        Solution ob;
        int ans = ob.LongestBitonicSequence(nums);
        cout << ans << "\n";
    }
    return 0;
} // } Driver Code Ends