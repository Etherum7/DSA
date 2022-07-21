import sys
class Solution:
    # def __init__(self):
    #     self.t=[[-1 for i in range(101)] for j in range(101)]
    # def util(self,arr, i ,j):
    #         res=float('inf')
    #         if i==j:
    #             return 0
    #         if self.t[i][j] !=-1:
    #             return self.t[i][j]
    #         self.t[i][j]= sys.maxsize
    #         for k in range(i, j):
    #             self.t[i][j]= min(self.t[i][j], self.util(arr, i, k)+ self.util(arr, k+1, j) + (arr[i-1]*arr[k]*arr[j]))
    #         return self.t[i][j]    
    
    def matrixMultiplication(self, N, arr):
        dp = [[0] * N for i in range(N)]
        for d in range(2, N):
            for i in range(N - d):
                j = i + d
                dp[i][j] = min(dp[i][k] + dp[k][j] + arr[i] * arr[j] * arr[k] for k in range(i + 1, j))
        return dp[0][N - 1]
        
        # return self.util(arr, 1, N-1) 
ob=Solution()
print(ob.matrixMultiplication(5,[10,5,20,10,5]))