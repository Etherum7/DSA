class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def isSafeB(self, x, y, A, B):
        afl = A//2
        

        return ( y < afl-B) or ( y > afl+B) or (x < afl-B ) or (x > afl+B )

    def isSafe(self, x, y, A, B, visited):
        # print(self.isSafeB(x,y, A, B))
        return x >= 0 and y >= 0 and x < A and y < A and  self.isSafeB(x, y, A, B)  
        

    def traverse(self, x, y, A, B, cnt, visited):
        # visited.add((x, y))
        if x == A-1 and y == A-1:
            cnt[0] += 1
            # visited.remove((x, y))
            return
        dx = [1, 0]
        dy = [0, 1]
        for k in range(2):
            newx = dx[k]+x
            newy = dy[k]+y
            if self.isSafe(newx, newy, A, B, visited):
                
                self.traverse(newx, newy, A, B, cnt, visited)
        # visited.remove((x, y))

    def solve(self, A, B):
        
        cnt = [0]
        visited = set()
        self.traverse(0, 0, A, B, cnt, visited)
        return cnt[0]
ob=Solution()
print(ob.solve(11,4))