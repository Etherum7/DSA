class Solution:
    def subsetSum(self, arr, N, s):
        t=[[ True if i==0 else False for i in range(s+1)] for j in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, s+1):
                if arr[i-1]>j:
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
        return t[N][s]
    
    def equalPartition(self, N, arr):
        if sum(arr)%2!=0:
            return 0
        if self.subsetSum(arr, N, sum(arr)//2):
            return 1
        else:
            return 0