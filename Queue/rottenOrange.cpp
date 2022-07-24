#include <bits/stdc++.h>
using namespace std;
int orangesRotting(vector<vector<int>> &grid)
{
    if (grid.empty())
        return 0;
    int m = grid.size(), n = grid[0].size(), days = 0, tot = 0, cnt = 0;
    queue<pair<int, int>> rotten;
    for (int i = 0; i < m; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            if (grid[i][j] != 0)
                tot++;
            if (grid[i][j] == 2)
                rotten.push({i, j});
        }
    }

    int dx[4] = {0, 0, 1, -1};
    int dy[4] = {1, -1, 0, 0};

    while (!rotten.empty())
    {
        int k = rotten.size();
        cnt += k;
        while (k--)
        {
            int x = rotten.front().first, y = rotten.front().second;
            rotten.pop();
            for (int i = 0; i < 4; ++i)
            {
                int nx = x + dx[i], ny = y + dy[i];
                if (nx < 0 || ny < 0 || nx >= m || ny >= n || grid[nx][ny] != 1)
                    continue;
                grid[nx][ny] = 2;
                rotten.push({nx, ny});
            }
        }
        if (!rotten.empty())
            days++;
    }

    return tot == cnt ? days : -1;
}

int main()
{
    vector<vector<int>> v{{2, 1, 1}, {1, 1, 0}, {0, 1, 1}};
    int rotting = orangesRotting(v);
    cout << "Minimum Number of Minutes Required " << rotting << endl;
}
class Solution
{
public:
    bool isSafe(int i, int j, int n, int m, vector<vector<int>> &grid)
    {
        return i >= 0 and i < n and j >= 0 and j < m and grid[i][j] == 1;
    }
    int orangesRotting(vector<vector<int>> &grid)
    {
        queue<pair<pair<int, int>, int>> q;
        int n = grid.size();
        int m = grid[0].size();
        int totalOrange = 0;
        int rottenOrange = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (grid[i][j] == 1)
                {
                    totalOrange += 1;
                }
                else if (grid[i][j] == 2)
                {
                    rottenOrange += 1;
                    totalOrange += 1;
                    q.push({{i, j}, 0});
                }
            }
        }
        vector<int> dx = {1, 0, 0, -1};
        vector<int> dy = {0, 1, -1, 0};
        int time = 0;
        while (!q.empty())
        {
            int x = q.front().first.first;
            int y = q.front().first.second;
            int t = q.front().second;
            q.pop();
            time = max(time, t);
            for (int k = 0; k < 4; k++)
            {
                int newX = x + dx[k];
                int newY = y + dy[k];

                if (isSafe(newX, newY, n, m, grid))
                {
                    rottenOrange += 1;
                    grid[newX][newY] = 2;
                    q.push({{newX, newY}, t + 1});
                }
            }
        }
        if (rottenOrange == totalOrange)
        {
            return time;
        }
        return -1;
    }
};