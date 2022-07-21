#include <bits/stdc++.h>
using namespace std;
// int f(int day, int last, vector<vector<int>> &points, vector<vector<int>> &dp)
// {
//     if (day == 0)
//     {
//         int maxi = 0;
//         for (int i = 0; i < 3; i++)
//         {
//             if (i != last)
//             {
//                 maxi = max(maxi, points[0][i]);
//             }
//             return maxi;
//         }
//         if (dp[day][last] != -1)
//         {
//             return dp[day][last];
//         }
//         maxi = 0;
//         for (int i = 0; i < 3; i++)
//         {
//             if (i != last)
//             {
//                 int point = points[day][i] + f(day - 1, i, points, dp);
//                 maxi = max(maxi, point);
//             }
//         }
//         return dp[day][last] = maxi;
//     }
// }
// int ninjaTraining(int n, vector<vector<int>> &points)
// {
//     // Write your code here.
//     vector<vector<int>> dp(n, vector<int>(4, -1));
//     return f(n, 3, points, dp);
// }

#include <bits/stdc++.h>
// using namespace std;
int ninjaTraining(int n, vector<vector<int>> &points)
{
    vector<vector<int>> dp(n, vector<int>(4, -1));
    dp[0][0] = max(points[0][1], points[0][2]);
    dp[0][1] = max(points[0][0], points[0][2]);
    dp[0][2] = max(points[0][1], points[0][0]);
    dp[0][3] = max(points[0][0], max(points[0][1], points[0][2]));

    for (int day = 1; day < n; day++)
    {
        for (int last = 0; last <= 3; last++)
        {
            int maxi = 0;
            for (int task = 0; task < 3; task++)
            {
                if (task != last)
                {
                    int point = points[day][task] + dp[day - 1][task];
                    maxi = max(maxi, point);
                }
            }
            dp[day][last] = maxi;
        }
    }
    return dp[n - 1][3];
}

// Space optimed
#include <bits/stdc++.h>
// using namespace std;
int ninjaTraining(int n, vector<vector<int>> &points)
{
    vector<int> dp(4, -1);
    vector<int> dummy(4, -1);
    dp[0] = max(points[0][1], points[0][2]);
    dp[1] = max(points[0][0], points[0][2]);
    dp[2] = max(points[0][1], points[0][0]);
    dp[3] = max(points[0][0], max(points[0][1], points[0][2]));

    for (int day = 1; day < n; day++)
    {
        for (int last = 0; last <= 3; last++)
        {
            int maxi = 0;
            for (int task = 0; task < 3; task++)
            {
                if (task != last)
                {
                    dummy[last] = max(dummy[last], points[day][task] + dp[task]);
                }
            }
        }
        dp = dummy;
    }
    return dp[3];
}