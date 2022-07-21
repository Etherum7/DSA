from bisect import bisect_left


class Solution:
    # def lcs(self, a, b, n, m):
    #     t=[[0] * (m+1) for j in range(n+1)]
    #     for i in range(1, n+1):
    #          for j in range(1, m+1):
    #              if a[i-1]==b[j-1]:
    #                  t[i][j]=1+t[i-1][j-1]
    #              else:
    #                  t[i][j]= max(t[i-1][j], t[i][j-1])
    #     return t[n][m]

    # Function to find length of longest increasing subsequence.
    def longestSubsequence(self, a, n):
        # LIS=[1  for i in range(n+1)]
        # for i in range(n):
        #     for j in range(i):
        #         if a[j]<a[i]:
        #             LIS[i]= max(LIS[i], 1 + LIS[j])
        # return max(LIS)
        temp = []
        temp.append(a[0])
        l = 1
        for i in range(1, n):
            if a[i] > temp[-1]:
                temp.append(a[i])
                l += 1
            else:
                ind = bisect_left(temp, a[i])
                temp[ind] = a[i]

        return l
