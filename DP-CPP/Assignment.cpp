// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{
public:
    int f(int person, vector<int> &done, int *Arr, int N)
    {
        if (person == -1)
        {
            return 0;
        }
        int start = person * N;
        int mini = INT_MAX;
        for (int i = start; i < start + N; i++)
        {
            if (done[i - start] == 0)
            {
                done[i - start] = 1;
                int cost = Arr[i] + f(person - 1, done, Arr, N);
                mini = min(mini, cost);
                done[i - start] = 0;
            }
        }
        return mini;
    }
    int assignmentProblem(int Arr[], int N)
    {
        // code here
        vector<int> done(N, 0);
        return f(N - 1, done, Arr, N);
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