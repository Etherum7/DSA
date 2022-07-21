// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function template for C++

class Solution
{
public:
    // arr[] : int input array of integers
    // k : the quadruple sum required
    vector<vector<int>> fourSum(vector<int> &arr, int s)
    {
        // Your code goes here
        sort(arr.begin(), arr.end());
        vector<vector<int>> res;
        int n = arr.size();
        int i = 0;
        while (i < n)
        {
            int j = i + 1;
            while (j < n - 1)
            {
                int k = j + 1;
                int l = n - 1;
                int target = s - arr[i] - arr[j];
                while (k < l)
                {
                    int actual = arr[k] + arr[l];
                    if (actual == target)
                    {
                        res.push_back({arr[i], arr[j], arr[k], arr[l]});
                        int temp1 = arr[k];
                        int temp2 = arr[l];
                        while (k < l && arr[k] == temp1)
                        {
                            k++;
                        }
                        while (k < l && arr[l] == temp2)
                        {
                            l--;
                        }
                    }
                    else if (actual < target)
                    {
                        k += 1;
                    }
                    else
                    {
                        l -= 1;
                    }
                }
                int temp1 = arr[j];

                while (j < n and arr[j] == temp1)
                {
                    j++;
                }
            }
            int temp1 = arr[i];
            while (i < n and temp1 == arr[i])
            {
                i += 1;
            }
        }
        return res;
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k, i;
        cin >> n >> k;
        vector<int> a(n);
        for (i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        Solution ob;
        vector<vector<int>> ans = ob.fourSum(a, k);
        for (auto &v : ans)
        {
            for (int &u : v)
            {
                cout << u << " ";
            }
            cout << "$";
        }
        if (ans.empty())
        {
            cout << -1;
        }
        cout << "\n";
    }
    return 0;
} // } Driver Code Ends