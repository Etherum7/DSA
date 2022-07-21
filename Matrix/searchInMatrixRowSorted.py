# User function Template for python3
class Solution:
    def matSearch(self, mat, N, M, X):
        # Complete this function
        i = 0
        j = M-1
        while i < N and j >= 0:
            if mat[i][j] == X:
                return 1
            elif mat[i][j] > X:
                j -= 1
            else:
                i += 1
        return 0
# m+n