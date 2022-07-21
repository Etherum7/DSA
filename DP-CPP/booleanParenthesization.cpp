// class Solution{
// public:
// int f(int i, int j, int isTrue, string &S, vector<vector<vector<int>>> &dp){
//     if(i>j){
//         return 0;
//     }
//     if(dp[i][j][isTrue]!=-1) return dp[i][j][isTrue];
//     if(i==j){
//         if (isTrue){
//             return S[i]=='T';
//         }
//         else return S[i]=='F';
//     }
//     int ways=0;
//     for(int ind=i+1; ind<=j-1; ind+=2){
//         // cout<<ind<<' ';
//         int lT= f(i, ind-1, 1, S, dp);
//         int rT=f(ind+1, j, 1, S, dp);
//         int lF= f(i, ind-1, 0, S, dp);
//         int rF=f(ind+1, j, 0, S, dp);
//         if(S[ind]=='&'){
//             if (isTrue){
//                 ways+=lT*rT;
//             }
//             else{
//                 ways+=lT*rF+lF*rF+lF*rT;
//             }
//         }
//         else if(S[ind]=='|'){
//             if (isTrue){
//                 ways+=lT*rT +lF*rT+lT*rF;
//             }
//             else{
//                 ways+=lF*rF;
//             }
//         }
//         else if(S[ind]=='^'){
//             // cout<<"here"<<' ';
//             if (isTrue){
//                 ways+=lF*rT+lT*rF;
//             }
//             else{
//                 ways+=lT*rT + lF*rF;
//             }
//         }
//     }
//     return dp[i][j][isTrue]=ways%1003;
// }
//     int countWays(int N, string S){
//         // code here
//         vector<vector<vector<int>>> dp(N, vector<vector<int>>(N, vector<int>(2, -1)));

//         return f(0, N-1, 1, S, dp);
//     }
// };
// #include <bits/stdc++.h>
// using namespace std;

// int main()
// {

//     return 0;
// }

#include <bits/stdc++.h>
using namespace std;

int main()
{

    return 0;
}

// { Driver Code Starts
// Initial Template for C++



class Solution
{
public:

    int countWays(int N, string S)
    {
        // code here
        vector<vector<vector<int>>> dp(N + 1, vector<vector<int>>(N + 1, vector<int>(2, 0)));
        for (int i = N - 1; i >= 0; i--)
        {
            for (int j = i; j <N; j++)
            {
                // if (i > j)
                //     continue;
                for (int isTrue = 0; isTrue <= 1; isTrue++)
                {
                    if (i == j)
                    {
                        if (isTrue)
                        {
                            dp[i][j][isTrue] = S[i] == 'T';
                        }
                        else
                        {
                            dp[i][j][isTrue] = S[i] == 'F';
                        }
                        continue;
                    }
                    int ways = 0;
                    for (int ind = i + 1; ind <= j - 1; ind += 2)
                    {

                        // cout<<ind<<' ';
                        int lT = dp[i][ind - 1][1];
                        int rT = dp[ind + 1][j][1];
                        int lF = dp[i][ind - 1][0];
                        int rF = dp[ind + 1][j][0];
                        if (S[ind] == '&')
                        {
                            if (isTrue)
                            {
                                ways += lT * rT;
                            }
                            else
                            {
                                ways += lT * rF + lF * rF + lF * rT;
                            }
                        }
                        else if (S[ind] == '|')
                        {
                            if (isTrue)
                            {
                                ways += lT * rT + lF * rT + lT * rF;
                            }
                            else
                            {
                                ways += lF * rF;
                            }
                        }
                        else if (S[ind] == '^')
                        {
                            // cout<<"here"<<' ';
                            if (isTrue)
                            {
                                ways += lF * rT + lT * rF;
                            }
                            else
                            {
                                ways += lT * rT + lF * rF;
                            }
                        }

                        
                        
                    }
                    dp[i][j][isTrue] = ways % 1003;
                    // cout<<dp[i][j][isTrue];
                }
            }
        }
        return dp[0][N - 1][1];
    }
};