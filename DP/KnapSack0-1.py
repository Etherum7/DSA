# User function Template for python3

class Solution:
    # def __init__(self):
    #     self.t = [[-1 for i in range(W + 1)] for j in range(n + 1)]
    # Function to return max value that can be put in knapsack of capacity W.

    def knapSack(self, W, wt, val, n):
        if n == 0 or W == 0:
            return 0
        if self.t[n][W] != -1:
            return self.t[n][W]
        if wt[n-1] <= W:
            self.t[n][W] = max(val[n-1]+self.knapSack(W-wt[n-1], wt, val, n-1),
                               self.knapSack(W, wt, val, n-1))
            return self.t[n][W]
        elif wt[n-1] > W:
            self.t[n][W] = self.knapSack(W, wt, val, n-1)
            return self.t[n][W]

    def knapSackT(self, W, wt, val, n):
        t = [[0 for i in range(W+1)] for j in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, W+1):
                if wt[i-1] <= j:
                    t[i][j] = max(val[i-1]+t[i-1][j-wt[i-1]], t[i-1][j])
                else:
                    t[i][j] = t[i-1][j]
        return t[n][W]
ob=Solution()
print(ob.knapSackT(5, [1,2,3], [10,20,30],3))


def isSubsetSum( N, arr, sum):
    # code here
    t = [[True if i == 0 else False for i in range(
        sum+1)] for j in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, sum+1):
            if arr[i-1] > j:
                t[i][j] = t[i-1][j]
            else:
                t[i][j] = t[i-1][j-arr[i-1]] or t[i-1][j]
    return t[N][sum]
# print(isSubsetSum(4, [1,5,5,11], 10 ))
    # code here

# {
#  Driver Code Starts
# Initial Template for Python 3
# import atexit
# import io
# import sys

# Contributed by : Nagendra Jha

# if __name__ == '__main__':
#     test_cases = int(input())
#     for cases in range(test_cases):
#         n = int(input())
#         W = int(input())
#         val = list(map(int,input().strip().split()))
#         wt = list(map(int,input().strip().split()))
#         ob=Solution()
#         print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends
