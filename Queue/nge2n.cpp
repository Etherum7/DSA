#include <bits/stdc++.h>
using namespace std;


vector<int> nge(vector<int> &nums, int n)
{
    stack<int> st;
    vector<int> res(n, -1);

    for (int i = 2 * n - 1; i >= 0; i--)
    {
        while (!st.empty() and st.top() < nums[i % n])
        {
            st.pop();
        }
        if (i < n)
        {
            if (!st.empty())
            {
                res[i] = st.top();
                st.pop();
            }
        }
        st.push(nums[i % n]);
    }
    return res;
}

int main()
{
    vector<int> v{5, 7, 1, 2, 6, 0};
    vector<int> res = nge(v, 6);
    cout << "The next greater elements are" << endl;
    for (int i = 0; i < res.size(); i++)
    {
        cout << res[i] << " ";
    }
    return 0;
}
