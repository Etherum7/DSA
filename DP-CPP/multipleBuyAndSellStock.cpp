#include<bits/stdc++.h>

long getMaximumProfit(long *values, int n)
{
//     vector<vector<long>> dp(n+1, vector<long>(2, 0));
    vector<long>dp(2,0);
    vector<long>cur(2,0);
//     base case already
    for(int day=n-1;day>=0;day--){
        for(int canBuy=0;canBuy<=1;canBuy++){
            long profit=0;
            if(canBuy){
                 profit = max(-values[day]+dp[0], dp[1]);
            }
            else{
                profit=max(values[day]+dp[1], dp[0]);
            }
            cur[canBuy]=profit;
                }
        dp=cur;
    }
    return dp[1];
    //Write your code here
}
long getMaximumProfit(long *values, int n)
{
    vector<vector<long>> dp(n+1, vector<long>(2, 0));
//     base case already
    for(int day=n-1;day>=0;day--){
        for(int canBuy=0;canBuy<=1;canBuy++){
            long profit=0;
            if(canBuy){
                 profit = max(-values[day]+dp[day+1][0], dp[day+1][1]);
            }
            else{
                profit=max(values[day]+dp[day+1][1], dp[day+1][0]);
            }
            dp[day][canBuy]=profit;
                }
    }
    return dp[0][1];
    //Write your code here
}
long f(int day, int canBuy,int n, long *values ,  vector<vector<long>> &dp){
    if(day==n){
        return 0;
    }
    if(dp[day][canBuy]!=-1) return dp[day][canBuy];
    long profit=0;
    if(canBuy){
         profit = max(-values[day]+f(day+1, 0, n,values, dp), f(day+1, 1, n,values, dp));
    }
    else{
        profit=max(values[day]+f(day+1, 1, n,values, dp), f(day+1, 0, n,values, dp));
    }
    return dp[day][canBuy]=profit;
}
long getMaximumProfit(long *values, int n)
{
    vector<vector<long>> dp(n+1, vector<long>(2, -1));
    return f(0, 1, n, values, dp);
    //Write your code here
}
#include <bits/stdc++.h>
using namespace std;

int main()
{
    
    return 0;
}