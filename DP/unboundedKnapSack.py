class Solution:
    def __init__(self):
        self.t=[[-1   for i in range(W+1)] for j in range(N+1)]
        
    
    def knapSack(self, N, W, val, wt):
        t=[[0 for i in range(W+1)] for j in range(N+1)]
        for i in range(N+1):
            for j in range(W+1):
                if wt[i-1]> j:
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]= max(val[i-1]+t[i][j-wt[i-1]] , t[i-1][j])
        return t[N][W]