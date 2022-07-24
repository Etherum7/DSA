#include <bits/stdc++.h>
using namespace std;

int main()
{
    
    return 0;
}
class Solution
{
public:
    vector<int> maxSlidingWindow(vector<int> &nums, int k)
    {
        deque<int> q;
        int i = 0;
        int j = 0;
        int n = nums.size();
        vector<int> res;
        while (j < n)
        {
            while (!q.empty() and q.back() < nums[j])
            {
                q.pop_back();
            }
            q.push_back(nums[j]);
            if (j - i + 1 == k)
            {
                res.push_back(q.front());
                if (q.front() == nums[i])
                {
                    q.pop_front();
                }
                i += 1;
            }

            j += 1;
        }
        return res;
    }
};