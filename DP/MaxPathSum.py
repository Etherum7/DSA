class Solution:
    def maximumPath(self, N, Matrix):
        # code here
        t=[[0 for i in range(N+1)] for j in range(N+1)]
        for i in range(N, 0, -1):
            for j in range(1, N+1):
                if i==N:
                    t[i][j]=Matrix[i-1][j-1]
                else:
                    if j==N:
                        right=0
                    else:
                        right=t[i+1][j+1]
                    down=t[i+1][j]
                    left=t[i+1][j-1]
                    t[i][j]=Matrix[i-1][j-1]+max(right, down, left)
        return max(t[1])