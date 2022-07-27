class Solution
{
public:
    bool f(int ind, int n, string A, unordered_set<string> st)
    {
        if (ind == n)
            return true;
        string temp = "";
        for (int j = ind; j < n; j++)
        {
            temp += A[j];

            if (st.find(temp) != st.end())
            {
                // cout<<' '<<temp;
                if (f(j + 1, n, A, st))
                {

                    return true;
                }
            }
        }
        return false;
    }
    int wordBreak(string A, vector<string> &B)
    {
        // code here

        unordered_set<string> st(B.begin(), B.end());
        int n = A.size();
        return f(0, n, A, st);
    }
};