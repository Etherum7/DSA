# User function Template for python3

class Solution:
    def isSafe(self, i, j, side, R, C):
        return side+i < R and side+j < C and i-side >= 0 and j-side >= 0
    # def largestSquare(self, M, R, C, K, Q, q_i, q_j):
    #     # code here
    #     for i in range(1, R):
    #         M[i][0]+=M[i-1][0]
    #     for j in range(1, C):
    #         M[0][j]+=M[0][j-1]
    #     for i in range(1, R):
    #         for j in range(1,C):
    #             M[i][j]=M[i-1][j]+M[i][j-1]-M[i-1][j-1]+M[i][j]
    #     res=[0]*Q
    #     for k in range(Q):
    #         i=q_i[k]
    #         j=q_j[k]
    #         mul=0
    #         while self.isSafe(i,j, mul, R,C):
    #             upSide=0
    #             leftSide=0
    #             twiceSide=0
    #             tli=tlj=rbj=rbi=0
    #             tli=i-mul
    #             tlj=j-mul
    #             rbi=i+mul
    #             rbj=j+mul
    #             if tli-1>=0:
    #                 upSide=M[tli-1][rbj]
    #             if tlj-1>=0:
    #                 leftide=M[rbi][tlj-1]
    #             if tli-1>=0 and tlj-1>=0:
    #                 twiceSide=M[tli-1][tlj-1]
    #             ans=M[rbi][rbj]-upSide-leftSide+twiceSide
    #             if ans>K:
    #                 break
    #             else:
    #                 res[k]=(2*mul)+1
    #             mul+=1
    #     return res

    def largestSquare(self, M, R, C, K, Q, q_i, q_j):
        # code here
        for i in range(1, R):
            M[i][0] += M[i-1][0]
        for i in range(1, C):
            M[0][i] += M[0][i-1]

        for i in range(1, R):
            for j in range(1, C):
                M[i][j] = M[i-1][j] + M[i][j-1] - M[i-1][j-1] + M[i][j]

        res = [0]*Q
        for k in range(Q):
            i = q_i[k]
            j = q_j[k]
            p = 0
            while(p+i < R and p+j < C and i-p >= 0 and j-p >= 0):
                a, b, c = 0, 0, 0
                if(j-p-1 >= 0):
                    a = M[i+p][j-p-1]
                if(i-p-1 >= 0):
                    b = M[i-p-1][j+p]
                if(j-p-1 >= 0 and i-p-1 >= 0):
                    c = M[i-p-1][j-p-1]

                ans = M[i+p][j+p] - a - b + c
                if ans > K:
                    break
                else:
                    res[k] = 2*p+1
                p += 1
        return res


# {
  # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        R, C = map(int, input().split())
        M = []

        for i in range(R):
            temp = list(map(int, input().split()))
            M.append(temp)

        K, Q = list(map(int, input().split()))

        q_i = list(map(int, input().split()))
        q_j = list(map(int, input().split()))

        ob = Solution()
        res = ob.largestSquare(M, R, C, K, Q, q_i, q_j)

        for i in res:
            print(i, end=" ")
        print()
# } Driver Code Ends
