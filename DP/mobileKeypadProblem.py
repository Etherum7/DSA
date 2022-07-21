# User function Template for python3
class Solution:

    def getCount(self, N):
        # code here
        mob = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -1]]
        row = [0, -1, 0, 1, 0]
        col = [0, 0, -1, 0, 1]
        t = [[1 if i == 1 else 0 for i in range(N+1)] for j in range(10)]
        for k in range(2, N+1):
            for i in range(4):
                for j in range(3):
                    if mob[i][j] != -1:
                        num = mob[i][j]
                        for move in range(5):
                            ro = i+row[move]
                            co = j+col[move]

                            if ro >= 0 and co >= 0 and ro < 4 and co < 3 and mob[ro][co] != -1:
                                nextNum = mob[ro][co]
                                t[num][k] += t[nextNum][k-1]
        res = 0
        for i in range(10):
            res += t[i][N]
        return res
