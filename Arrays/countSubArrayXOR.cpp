#include <bits/stdc++.h>
int subarraysXor(vector<int> &arr, int x)
{
    //    Write your code here.
    int XR = 0;
    int cnt = 0;
    map<int, int> mp;
    int n = arr.size();
    for (int i = 0; i < n; i++)
    {
        XR = XR ^ arr[i];
        if (XR == x)
        {
            cnt += 1;
        }
        if (mp.find(XR ^ x) != mp.end())
        {
            cnt += mp[XR ^ x];
        }
        mp[XR] += 1;
    }
    return cnt;
}