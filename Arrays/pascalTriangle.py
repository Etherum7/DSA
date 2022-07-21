class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]*(i+1) for i in range(numRows)]
        # res[0]=1
        for row in range(2, numRows):
            for j in range(1, row):
                res[row][j] = res[row-1][j-1]+res[row-1][j]
        return res
# User function Template for python3


class Solution:

    def nthRowOfPascalTriangle(self, n):
        # code here
        res = [[1]*(i+1) for i in range(n)]
        for row in range(2, n):
            for j in range(1, row):
                res[row][j] = (res[row-1][j-1]+res[row-1][j]) % (10**9+7)
       # for i in range(len(res[-1])):
       #     res[-1][i]=res[-1][i]
        return res[-1]
