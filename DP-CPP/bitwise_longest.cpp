#include <bits/stdc++.h>
using namespace std;

int isValid(int i, int j, vector<int> &arr)
{
    return (arr[i] & arr[j]) * 2 < (arr[i] | arr[j]);
}
int f(int ind, int prev_ind, vector<int> &arr, int n, vector<vector<int>> dp)
{
    if (ind == n)
        return 0;
    int len1 = 0 + f(ind + 1, prev_ind, arr, n, dp);
    int len2 = 0;
    if (prev_ind == -1 or isValid(prev_ind, ind, arr))
    {   
        len2 = 1 + f(ind + 1, ind, arr, n, dp);
    }
    return max(len1, len2);
}
int LIS(vector<int> &arr, int n)
{
    vector<int> parent(n, -1);
    vector<vector<int>> dp(n, vector<int>(n+1, -1));
    return f(0, -1, arr, n, dp);
}

int main()
{
    vector<int> arr = {15, 6, 5, 12, 1};
    
    int val = LIS(arr, 5);
    cout
        << val;

    // vector<int> arr1={17, 16, 12 , 2 , 8, 17, 17};
    return 0;
}
