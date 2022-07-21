// { Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

// } Driver Code Ends
// User function template for C++

class Solution
{
public:
int findMaxSum(int *arr, int n) {
	    // code here
	    
	    int prev2=arr[0];
	    if (n==1){
	        return prev2;
	    }
	    
	    int prev1=max(arr[0], arr[1]);
	    for (int i=2;i<n;i++){
	        int curi=max(prev2+arr[i], prev1);
	        prev2=prev1;
	        prev1=curi;
	    }
	    return prev1;
	    
	    
	    
	}
    // calculate the maximum sum with out adjacent
    int f(int ind, int *arr, vector<int> &dp)
    {
        if (ind == 0)
        {
            return arr[0];
        }
        if (ind < 0)
        {
            return 0;
        }
        if (dp[ind] != -1)
        {
            return dp[ind];
        }

        int pick = arr[ind] + f(ind - 2, arr, dp);
        int nonpick = f(ind - 1, arr, dp);

        dp[ind] = max(pick, nonpick);
        return dp[ind];
    }
    int findMaxSum(int *arr, int n)
    {
        // code here
        vector<int> dp(n, -1);
        return f(n - 1, arr, dp);
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
        int arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        Solution ob;
        auto ans = ob.findMaxSum(arr, n);
        cout << ans << "\n";
    }
    return 0;
} // } Driver Code Ends