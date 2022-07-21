class Solution:
    def subsetSum(self, arr,N, W):
        t=[[True if i==0 else False for i in range(W+1)] for j in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, W+1):
                if  arr[i-1]>j:
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]= t[i-1][j-arr[i-1]] or t[i-1][j]
        return t[N][W]
   
    def equalPartition(self, N, arr):
        s=sum(arr)
        if s%2!=0:
            return 0
        return self.subsetSum(arr, N, s//2)