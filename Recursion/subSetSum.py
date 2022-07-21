class Solution:
    def util(self, i, arr, N, res, op):
        if i == N:
            res.append(op)
            return
        self.util(i+1, arr, N, res, op+arr[i])
        self.util(i+1, arr, N, res, op)

    def subsetSums(self, arr, N):
        # code here
        res = []
        self.util(0, arr, N, res, 0)
        return res
