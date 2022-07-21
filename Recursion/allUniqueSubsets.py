class Solution:
    def util(self, i, arr, res, n, op) :
        res.append(op)
        for j in range(i,n ):
            if j!=i and arr[j]==arr[j-1]:
                continue
            op1=op.copy()
            op1.append(arr[j])
            self.util(j+1, arr, res, n, op1)
    #Function to find all possible unique subsets.
    def AllSubsets(self, arr,n):
        #code here
        arr.sort()
        res=[]
        op=[]
        self.util(0, arr, res, n, op)
        return res