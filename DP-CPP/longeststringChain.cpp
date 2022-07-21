class Solution
{
public:
    bool compareStrings(string &s1, string &s2)
    {
        if (s1.size() != s2.size() + 1)
            return false;
        int first = 0;
        int second = 0;
        while (first < s1.size())
        {
            if (second < s2.size() && s1[first] == s2[second])
            {
                first += 1;
                second += 1;
            }
            else
            {
                first++;
            }
        }
        return second == s2.size();
    }
    static bool compare(string &s1, string &s2)
    {
        return s1.size() < s2.size();
    }
    int longestStrChain(vector<string> &words)
    {
        int n = words.size();
        vector<int> dp(n, 1);
        int maxTill = 1;
        // vector<int> cur(n+1, 0);
        sort(words.begin(), words.end(), compare);
        for (int ind = 0; ind < n; ind++)
        {
            for (int prev_ind = 0; prev_ind < ind; prev_ind++)
            {
                if (compareStrings(words[ind], words[prev_ind]) &&
                    dp[ind] < 1 + dp[prev_ind])
                {

                    dp[ind] = 1 + dp[prev_ind];
                    maxTill = max(maxTill, dp[ind]);
                }
            }
        }
        // your code here
        return maxTill;
    }
};