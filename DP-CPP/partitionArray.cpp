
bool helper(int ind, int k, int m, vector<int> &A, vector<int> &dp)
{
    bool flag = false;
    if (ind <= -1)
        return true;
    if (dp[ind] != -1)
        return dp[ind];
    for (int i = ind - k + 1; i >= 0 && A[ind] - A[i] <= m; i--)
    {
        flag = flag | helper(i - 1, k, m, A, dp);
        if (flag == true)
        {
            break;
        }
    }
    dp[ind] = flag ? 1 : 0;
    return flag;
}
bool partitionArray(int N, int K, int M, vector<int> &A)
{
    sort(A.begin(), A.end());
    vector<int> dp(N, -1);
    helper(N - 1, K, M, A, dp);
    return dp[N - 1];
}
class Solution
{
public: // Dynamic Programming (Approach)
    bool partitionArray(int N, int K, int M, vector<int> &A)
    {
        // code here
        bool Dp[N + 1] = {0};
        Dp[0] = 1;
        sort(begin(A), end(A));
        for (int i = K; i <= N; ++i)
        {
            int j = lower_bound(begin(A), end(A), A[i - 1] - M) - begin(A);
            for (int n = j; n <= i - K; ++n)
            {
                Dp[i] = Dp[i] || Dp[n];
                if (Dp[i])
                {
                    break;
                }
            }
        }
        return Dp[N];
    }
};

class Solution
{
public:
    bool util(int temp, int N, int K, int M, vector<int> &A)
    {
        if (temp >= N)
            return true;
        if (N - temp < K)
            return false;
        for (int i = temp + K - 1; i < N; i++)
        {
            if (A[i] - A[temp] > M)
                return 0;
            if (util(i + 1, N, K, M, A))
            {
                return true;
            }
        }
        return 0;
    }
    bool partitionArray(int N, int K, int M, vector<int> &A)
    {
        sort(A.begin(), A.end());
        return util(0, N, K, M, A);
    }
};