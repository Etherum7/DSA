# # User function Template for python3

# class Solution:
#     def isSafe(self, loc, m, n, visited):

#         if loc[0] == -1 or loc[0] == n or loc[1] == -1 or loc[1] == n or visited[loc[0]][loc[1]] == True or m[loc[0]][loc[1]] == 0:
#             return False
#         return True

#     def util(self, loc, m, n, op, res, visited):
#         if (loc[0] == -1 or loc[0] == n or loc[1] == -1 or loc[1] == n or visited[loc[0]][loc[1]] == True or m[loc[0]][loc[1]] == 0):
#             return
#         if loc[0] == n-1 and loc[1] == n-1:
#             res.append(op)
#             return
#         print(loc)

#         visited[loc[0]][loc[1]] = True

#         if self.isSafe((loc[0]+1, loc[1]), m, n, visited):
#             self.util((loc[0]+1, loc[1]), m, n, op+'D', res, visited)
#         if self.isSafe((loc[0], loc[1]-1), m, n, visited):
#             self.util((loc[0], loc[1]-1), m, n, op+'L', res, visited)
#         if self.isSafe((loc[0], loc[1]+1), m, n, visited):
#             self.util((loc[0], loc[1]+1), m, n, op+'R', res, visited)
#         if self.isSafe((loc[0]-1, loc[1]), m, n, visited):
#             self.util((loc[0]-1, loc[1]), m, n, op+'U', res, visited)
#         visited[loc[0]][loc[1]] = False
#         return
#     def findPath(self, m, n):
#         # code here
#         res = []
#         if m[n-1][n-1] == 0 or m[0][0] == 0:
#             return []
#         visited = [[False for _ in range(n)] for _ in range(n)]
#         self.util((0, 0), m, n, '', res, visited)
#         return [] if len(res) == 0 else res

# User function Template for python3

# User function Template for python3

class Solution:
    def util(self, x, y, m, res, N, dirx, diry, dirn, vis, op):
        if x == N-1 and y == N-1:
            res.append(op)
            return
        for k in range(4):
            newx = x+dirx[k]
            newy = y+diry[k]
            if newx >= 0 and newx < N and newy >= 0 and newy < N and m[newx][newy] == 1 and not vis[newx][newy]:
                vis[x][y] = True
                self.util(newx, newy, m, res, N, dirx,
                          diry, dirn, vis, op+dirn[k])
                vis[x][y] = False

    def findPath(self, m, n):
        # code here
        res = []
        if m[0][0] == 0:
            return []
        dirn = ['D', 'L', 'R', 'U']
        diry = [0, -1, 1, 0]
        dirx = [1, 0, 0, -1]
        vis = [[False]*n for _ in range(n)]
        self.util(0, 0, m, res, n, dirx, diry, dirn, vis, '')
        return res
