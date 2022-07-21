#include <bits/stdc++.h>
using namespace std;

int main()
{

    return 0;
}
class Solution
{
public:
    int cutRod(int price[], int n)
    {
        // code here
        //  vector<vector<int>> dp(n, vector<int>(n+1, -1));
        vector<int> dp(n + 1, -1);
        for (int l = 0; l <= n; l++)
        {
            dp[l] = l * price[0];
        }
        for (int ind = 1; ind < n; ind++)
        {
            for (int length = 0; length <= n; length++)
            {
                int rodLength = ind + 1;
                int nontake = 0 + dp[length];
                int take = 0;
                if (rodLength <= length)
                {
                    take = price[ind] + dp[length - rodLength];
                }
                dp[length] = max(take, nontake);
            }
        }
        return dp[n];
    }

    int f(int ind, int length, int *price, vector<vector<int>> &dp)
    {
        if (ind == 0)
        {
            return length * price[0];
        }
        if (dp[ind][length] != -1)
        {
            return dp[ind][length];
        }
        int rodLength = ind + 1;
        int nontake = 0 + f(ind - 1, length, price, dp);
        int take = 0;
        if (rodLength <= length)
        {
            take = price[ind] + f(ind, length - rodLength, price, dp);
        }
        return dp[ind][length] = max(take, nontake);
    }
    int cutRod(int price[], int n)
    {
        // code here
        vector<vector<int>> dp(n, vector<int>(n + 1, -1));

        return f(n - 1, n, price, dp);
    }
};
