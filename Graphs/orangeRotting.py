# # include<bits/stdc++.h>
from queue import Queue
# using namespace std
# int orangesRotting(vector < vector < int >> & grid) {
#     if(grid.empty()) return 0
#     int m = grid.size(), n = grid[0].size(), days = 0, tot = 0, cnt = 0
#     queue < pair < int, int >> rotten
#     for(int i=0
#         i < m
#         + +i){
#         for(int j=0
#             j < n
#             + +j){
#             if(grid[i][j] != 0) tot++
#             if(grid[i][j] == 2) rotten.push({i, j})
#         }
#     }

#     int dx[4] = {0, 0, 1, -1}
#     int dy[4] = {1, -1, 0, 0}

#     while(!rotten.empty()){
#         int k = rotten.size()
#         cnt += k
#         while(k--){
#             int x = rotten.front().first, y = rotten.front().second
#             rotten.pop()
#             for(int i=0
#                 i < 4
#                 + +i){
#                 int nx = x + dx[i], ny = y + dy[i]
#                 if(nx < 0 | | ny < 0 | | nx >= m | | ny >= n | | grid[nx][ny] != 1) continue
#                 grid[nx][ny] = 2
#                 rotten.push({nx, ny})
#             }
#         }
#         if(!rotten.empty()) days++
#     }

#     return tot == cnt ? days: -1
# }

# int main()
# {
#     vector < vector < int >> v{{2, 1, 1}, {1, 1, 0}, {0, 1, 1}}
#     int rotting = orangesRotting(v)
#     cout << "Minimum Number of Minutes Required " << rotting << endl
# }


class Solution:

    # Function to find minimum time required to rot all oranges.
    def orangesRotting(self, grid):
        # Code here
        goodOranges = set()
        rottenOranges = Queue()
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    goodOranges.add((i, j))
                elif grid[i][j] == 2:
                    rottenOranges.put((i, j, 0))
        dirnx = [0, 1, -1, 0]
        dirny = [1, 0, 0, -1]
        res = 0
        while not rottenOranges.empty():
            pos_i, pos_j, stage = rottenOranges.get()
            for k in range(4):
                newx = pos_i+dirnx[k]
                newy = pos_j+dirny[k]
                if newx >= 0 and newy >= 0 and newx < n and newy < m and grid[newx][newy] == 1:
                    grid[newx][newy] = 2
                    rottenOranges.put((newx, newy, stage+1))
                    res = stage+1
                    goodOranges.remove((newx, newy))
        if len(goodOranges):
            return -1
        else:
            return res


ob = Solution()
print(ob.orangesRotting([[0, 1, 2], [0, 1, 2], [2, 1, 1]]))
print(ob.orangesRotting([[2, 2, 0, 1]]))
