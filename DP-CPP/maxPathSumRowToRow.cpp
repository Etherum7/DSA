#include <bits/stdc++.h>
using namespace std;

int main()
{

    return 0;
}

// Space Optimized
class Solution
{
public:
    int maximumPath(int N, vector<vector<int>> Matrix)
    {
        // code here
        // vector<vector<int>> dp(N, vector<int>(N,-1));
        vector<int> dp(N, 0);
        vector<int> temp(N, 0);
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (i == 0)
                {
                    temp[j] = Matrix[i][j];
                }
                else
                {
                    int up = Matrix[i][j];
                    int dig1 = Matrix[i][j];
                    int dig2 = Matrix[i][j];
                    if (i > 0)
                    {
                        up += dp[j];
                        if (j > 0)
                        {
                            dig1 += dp[j - 1];
                        }
                        if (j < N - 1)
                        {
                            dig2 += dp[j + 1];
                        }
                    }
                    temp[j] = max(up, max(dig1, dig2));
                }
            }
            dp = temp;
        }
        int res = 0;
        for (int i = 0; i < N; i++)
        {
            res = max(res, temp[i]);
        }
        return res;
    }
};
class Solution
{
public:
    int maximumPath(int N, vector<vector<int>> Matrix)
    {
        // code here
        vector<vector<int>> dp(N, vector<int>(N, -1));
        for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < N; j++)
            {
                if (i == 0)
                {
                    dp[i][j] = Matrix[i][j];
                }
                else
                {
                    int up = Matrix[i][j];
                    int dig1 = Matrix[i][j];
                    int dig2 = Matrix[i][j];
                    if (i > 0)
                    {
                        up += dp[i - 1][j];
                        if (j > 0)
                        {
                            dig1 += dp[i - 1][j - 1];
                        }
                        if (j < N - 1)
                        {
                            dig2 += dp[i - 1][j + 1];
                        }
                    }
                    dp[i][j] = max(up, max(dig1, dig2));
                }
            }
        }
        int res = 0;
        for (int i = 0; i < N; i++)
        {
            res = max(res, dp[N - 1][i]);
        }
        return res;
    }
};