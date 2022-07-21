// { Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
// User function template in C++

class Solution
{
public:
    // A1[] : the input array-1
    // N : size of the array A1[]
    // A2[] : the input array-2
    // M : size of the array A2[]

    // Function to sort an array according to the other array.
    vector<int> sortA1ByA2(vector<int> A1, int N, vector<int> A2, int M)
    {
        // Your code here
        map<int, int> mp;
        for (int i = 0; i < N; i++)
        {
            mp[A1[i]] += 1;
        }
        int i = 0;
        int j = 0;
        while (i < M)
        {
            while (i < M - 1 and A2[i] == A2[i + 1])
            {
                i += 1;
            }
            if (mp.find(A2[i]) != mp.end())
            {
                int cnt = mp[A2[i]];
                while (cnt > 0)
                {
                    A1[j] = A2[i];
                    cnt -= 1;
                    j += 1;
                }
                mp.erase(A2[i]);
            }
            i += 1;
        }
        for (auto it : mp)
        {
            int cnt = it.second;
            while (cnt)
            {
                A1[j] = it.first;
                j += 1;
                cnt -= 1;
            }
        }
        return A1;
    }
};

// { Driver Code Starts.

int main(int argc, char *argv[])
{

    int t;

    cin >> t;

    while (t--)
    {

        int n, m;
        cin >> n >> m;

        vector<int> a1(n);
        vector<int> a2(m);

        for (int i = 0; i < n; i++)
        {
            cin >> a1[i];
        }

        for (int i = 0; i < m; i++)
        {
            cin >> a2[i];
        }

        Solution ob;
        a1 = ob.sortA1ByA2(a1, n, a2, m);

        for (int i = 0; i < n; i++)
            cout << a1[i] << " ";

        cout << endl;
    }
    return 0;
}
// } Driver Code Ends