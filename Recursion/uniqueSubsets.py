# User function Template for python3

class Solution:

    # Function to find all possible unique subsets.
    def util(self, i, arr, n, res, op):
        if i > n:
            return
        if i == n:
            res.append(op)
            return
        op1 = op.copy()
        op1.append(arr[i])
        self.util(i+1, arr, n, res, op)
        self.util(i+1, arr, n, res, op1)

    def AllSubsets(self, arr, n):
        # code here
        arr.sort()
        res = []
        self.util(0, arr, n, res, [])
        return res
ob=Solution()
print(ob.AllSubsets([2,1,2],3))