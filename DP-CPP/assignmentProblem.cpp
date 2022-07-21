// tle
// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
public:
    int f(int person, long done, int *Arr, int N, vector<vector<long>> &dp)
    {
        if (person == -1)
        {
            return 0;
        }
        if (dp[person][done] != -1)
            return dp[person][done];
        int start = person * N;
        int mini = INT_MAX;
        for (int i = start; i < start + N; i++)
        {
            long val = (done >> (i - start)) & 1;
            //   cout<<val<<' ';
            if (val == 0)
            {
                done = done | 1 << (i - start);
                //   cout<<done<<" ";
                int cost = Arr[i] + f(person - 1, done, Arr, N, dp);
                mini = min(mini, cost);
                done = done & ~(1 << (i - start));
            }
        }
        return dp[person][done] = mini;
    }
    int assignmentProblem(int Arr[], int N)
    {
        // code here
        // vector<int> done(N,0);
        vector<vector<long>> dp(N, vector<long>(1 << N, -1));
        long done = 0;
        // done=done<<N;
        return f(N - 1, done, Arr, N, dp);
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

        int Arr[n * n];
        for (int i = 0; i < n * n; i++)
            cin >> Arr[i];

        Solution ob;
        cout << ob.assignmentProblem(Arr, n) << endl;
    }
    return 0;
} // } Driver Code Ends