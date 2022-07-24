#include <bits/stdc++.h>
using namespace std;

int main()
{
    
    return 0;
}
class Solution
{
public:
    void computeLPS(vector<int> &lps, string &needle, int M)
    {
        lps[0] = 0;
        int prevLenLps = 0;
        int i = 1;
        while (i < M)
        {
            if (needle[i] == needle[prevLenLps])
            {
                prevLenLps += 1;
                lps[i] = prevLenLps;
                i += 1;
            }
            else
            {
                if (prevLenLps != 0)
                {
                    prevLenLps = lps[prevLenLps - 1];
                }
                else
                {
                    lps[i] = 0;
                    i += 1;
                }
            }
        }
    }
    int strStr(string haystack, string needle)
    {
        int M = needle.size();
        int N = haystack.size();
        vector<int> lps(M, 0);
        computeLPS(lps, needle, M);
        int i = 0;
        int j = 0;
        while ((N - i) >= (M - j))
        {
            if (needle[j] == haystack[i])
            {
                i += 1;
                j += 1;
            }
            if (j == M)
            {
                return i - j;
            }
            else if (i < N && needle[j] != haystack[i])
            {
                if (j != 0)
                {
                    j = lps[j - 1];
                }
                else
                {
                    i += 1;
                }
            }
        }
        return -1;
    }
};