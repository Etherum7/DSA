
class Solution:

 def longestSubsequence(self, n, arr):
 
        lis=[1]*n
        for i in range(n):
            for j in range(i):
                if abs(arr[i]- arr[j])==(1):
                    lis[i]=max(lis[i],1+lis[j] )
        return max(lis)
