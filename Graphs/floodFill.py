import sys


class Solution:
    def isSafe(self, r, c, visited, n, m, col):
        return r >= 0 and r < n and c >= 0 and c < m and not visited[r][c] and image[r][c] == col

    def traverse(self, r, c, n, m, image, visited, newColor, col):
        visited[r][c] = True
        if image[r][c] == col:
            image[r][c] = newColor
        x = [0, 1, -1, 0]
        y = [1, 0, 0, -1]
        for k in range(4):
            if self.isSafe(r+x[k], c+y[k], visited, n, m, col):
                self.traverse(r+x[k], c+y[k], n, m, image,
                              visited, newColor, col)

    def floodFill(self, image, sr, sc, newColor):
        # Code here
        n = len(image)
        m = len(image[0])
        col = image[sr][sc]

        visited = [[False]*m for _ in range(n)]
        self.traverse(sr, sc, n, m, image, visited, newColor, col)
        return image


# {
#  Driver Code Starts
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        image = []
        for _ in range(n):
            image.append(list(map(int, input().split())))
        sr, sc, newColor = input().split()
        sr = int(sr)
        sc = int(sc)
        newColor = int(newColor)
        obj = Solution()
        ans = obj.floodFill(image, sr, sc, newColor)
        for _ in ans:
            for __ in _:
                print(__, end=" ")
            print()
# } Driver Code Ends
