# Review
class Solution:
    def numOfSubsets(self, arr, N, K):
        # code here 
        t=[[0]*(K+1) for j in range(N+1)]
        for i in range(1, N+1):
            for j in range(1, K+1):
                if arr[i-1]>j:
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]=1+ t[i-1][j//(arr[i-1])]+t[i-1][j]
        return t[N][K]