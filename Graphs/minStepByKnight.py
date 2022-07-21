from queue import Queue
import sys
sys.setrecursionlimit(10**5)


class Solution:

    def bfs(self, item, dst, N, visited, q):
        q.put(item)
        visited.add(item[0])
        cnt = 0
        moves = [[2, 1], [-2, -1], [2, -1], [-2, 1],
                 [1, 2], [1, -2], [-1, 2], [-1, -2]]

        while not q.empty():
            t = q.get()
            print(t, dst)
            if t[0] == dst:
                return t[1]
            for move in moves:
                i = t[0][0]+move[0]
                j = t[0][1]+move[1]
                if i > 0 and i <= N and j > 0 and j <= N:
                    if (i, j) not in visited:
                        q.put(((i, j), t[1]+1))
                        visited.add((i, j))
            

        return -1

    # Function to find out minimum steps Knight needs to reach target position.

    def minStepToReachTarget(self, KnightPos, TargetPos, N):
        # Code here
        #         if KnightPos==TargetPos:
        #             return 0
        visited = set()
        q = Queue()
        return self.bfs(((KnightPos[0], KnightPos[1]), 0), (TargetPos[0], TargetPos[1]), N, visited, q)


ob=Solution()
print(ob.minStepToReachTarget([4,5],[1,1],6))