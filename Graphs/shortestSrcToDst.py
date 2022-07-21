# User function Template for python3
from collections import deque


class Solution:

    def shortestDistance(self, N, M, A, X, Y):
        # code here
        q = deque()

        if A[0][0] == 0 or A[X][Y] == 0:
            return -1
        q.append((0, 0))
        dst = -1
        found = False
        dx = [1, 0, 0, -1]
        dy = [0, -1, 1, 0]
        A[0][0] = 0
        while len(q) and not found:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node[0] == X and node[1] == Y:
                    found = True
                    break
                for k in range(4):
                    newx = dx[k]+node[0]
                    newy = dy[k]+node[1]
                    if newx >= 0 and newy >= 0 and newx < N and newy < M and A[newx][newy]:
                        q.append((newx, newy))
                        A[newx][newy] = 0

            dst += 1
        return dst if found else -1
