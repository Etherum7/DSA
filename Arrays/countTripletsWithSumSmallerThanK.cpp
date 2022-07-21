// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution
{

public:
    long long countTriplets(long long arr[], int n, long long sum)
    {
        // Your code goes here
        int cnt = 0;
        sort(arr, arr + n);
        for (int start = 0; start <= n - 3; start++)
        {
            int i = start + 1;
            int j = n - 1;
            while (i < j)
            {
                if (arr[start] + arr[i] + arr[j] < sum)
                {
                    // cout<<start<<' '<<i<<' '<<j<<' ';
                    cnt += (j - i);
                    i += 1;
                }
                else
                {
                    j -= 1;
                }
            }
        }
        return cnt;
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
        long long sum;
        cin >> n >> sum;
        long long arr[n];
        for (int i = 0; i < n; i++)
        {
            cin >> arr[i];
        }

        Solution ob;
        cout << ob.countTriplets(arr, n, sum);

        cout << "\n";
    }
    return 0;
}

// } Driver Code Ends