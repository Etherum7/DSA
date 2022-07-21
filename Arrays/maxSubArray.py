class Solution:
    def maximumSumSubarray(self, K, Arr, N):
        # code here
        i = j = 0
        s = 0
        mx = -float('inf')
        while j < N:
            s = s+Arr[j]
            if j-i+1 < K:
                j += 1
            elif j-i+1 == K:
                mx = max(mx, s)
                s -= Arr[i]
                i += 1
                j += 1
        return mx
        
