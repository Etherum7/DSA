class Solution
{
public:
    bool f(int ind, int *A, int N, vector<int> &dp)
    {
        if (ind >= N - 1)
            return 1;
        if (A[ind] == 0)
            return 0;
        if (dp[ind] != -1)
            return dp[ind];
        for (int j = 1; j <= A[ind]; j++)
        {
            if (f(j + ind, A, N, dp))
                return true;
        }
        return dp[ind] = false;
    }
    int canReach(int A[], int N)
    {
        // code here
        vector<int> dp(N + 1, -1);
        return f(0, A, N, dp);
    }
};