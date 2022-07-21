class Solution
{
public:
    int smallestSumSubarray(vector<int> &a)
    {
        // Code here
        int i = 0;
        int j = 0;
        int n = a.size();
        int ans = INT_MAX;
        int cur = 0;
        while (j < n)
        {
            cur += a[j];
            while (cur > a[j])
            {
                cur -= a[i];
                i++;
            }
            ans = min(ans, cur);
            j += 1;
        }
        return ans;
    }
};

#include <bits/stdc++.h>
using namespace std;

int main()
{
    
    return 0;
}