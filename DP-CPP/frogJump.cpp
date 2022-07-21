// #include <cmath>
#include <bits/stdc++.h>
// using namespace std;
int frogJump(int n, vector<int> &heights)
{
    // Write your code here.
    if (n == 1)
    {
        return 0;
    }
    if (n == 2)
    {
        return abs(heights[1] - heights[0]);
    }
    int prev2 = 0;
    int prev1 = abs(heights[1] - heights[0]);

    for (int i = 2; i < n; i++)
    {
        int secondLast = prev2 + abs(heights[i] - heights[i - 2]);
        int last = prev1 + abs(heights[i] - heights[i - 1]);

        int curMinEnergy = std::min(secondLast, last);
        prev2 = prev1;
        prev1 = curMinEnergy;
    }
    return prev1;
}
