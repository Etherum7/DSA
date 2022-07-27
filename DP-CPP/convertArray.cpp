// Approac 1
class Solution
{
public:
    int lcs(int i, int j, int *A, int *B, vector<vector<long long>> &dp)
    {
        if (i < 0 or j < 0)
            return 0;
        if (dp[i][j] != -1)
            return dp[i][j];
        if (A[i] == B[j])
        {
            return dp[i][j] = 1 + lcs(i - 1, j - 1, A, B, dp);
        }
        else
        {
            return dp[i][j] = max(lcs(i - 1, j, A, B, dp), lcs(i, j - 1, A, B, dp));
        }
    }
    int minInsAndDel(int A[], int B[], int N, int M)
    {
        // code here
        vector<long long> dp(M + 1);
        vector<long long> cur(M + 1);

        for (int i = 1; i <= N; i++)
        {
            for (int j = 1; j <= M; j++)
            {
                if (A[i - 1] == B[j - 1])
                {
                    cur[j] = 1 + dp[j - 1];
                }
                else
                {
                    cur[j] = max(dp[j], cur[j - 1]);
                }
            }
            dp = cur;
        }
        return N + M - 2 * dp[M];
    }
};