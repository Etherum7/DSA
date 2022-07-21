from collections import defaultdict


class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        i = 0
        j = 0
        cmap = defaultdict(int)
        cnt = 0
        res = []
        while j < N:
            cmap[A[j]] += 1
            if cmap[A[j]] == 1:
                cnt += 1
            if j-i+1 < K:
                j += 1
            else:
                res.append(cnt)
                cmap[A[i]] -= 1
                if cmap[A[i]] == 0:
                    cnt -= 1
                i += 1
                j += 1
        return res
