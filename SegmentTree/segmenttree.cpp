#include <bits/stdc++.h>
using namespace std;
// vector<int> arr;
// int n = arr.size();
// vector<int> seg(4 * n, 0);
// void build(int ind, int low, int high)
// {
//     if (low == high)
//     {
//         seg[ind] = arr[low];
//         return;
//     }
//     int mid = (low + high) / 2;
//     build(2 * ind + 1, low, mid);
//     build(2 * ind + 2, mid + 1, high);
//     seg[ind] = max(seg[2 * ind + 1], seg[2 * ind + 2]);
//     return;
// }
// int query(int ind, int low, int high, int l, int r)
// {

//     if (l <= low and r >= high)
//     {
//         return seg[ind];
//     }
//     if (low > r || high < l)
//     {
//         return INT_MIN;
//     }
//     int mid = (low + high) / 2;
//     return max(query(2 * ind + 1, low, mid, l, r), query(2 * ind + 2, mid + 1, high, l, r));
// }
int main()
{
    // build(0, 0, n - 1);
    // int q;
    // cin >> q;
    // while (q--)
    // {
    //     int l, r;
    //     cin >> l >> r;
    //     cout << query(0, 0, n - 1, l, r);
    // }
    vector<int> res;
    int N;
    cin >> N;
    // cout << N << endl;
    // string str;
    // stringstream ss(cin);
    // int cur;
    int temp;
    do
    {
        cin >> temp;
        res.push_back(temp);

N-=1;
    } while (N);
    
    return 0;
}