class Solution:
    def dfs(self, i, j, vis, grid, n, m):
        vis[i][j] = True

        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and not vis[ni][nj] and grid[ni][nj] == '1':
                self.dfs(ni, nj, vis, grid, n, m)

    def numIslands(self, grid):
        islands = 0
        n = len(grid)
        m = len(grid[0])

        vis = []
        for i in range(n):
            row = []
            for j in range(m):
                row.append(False)
            vis.append(row)

        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j] == '1':
                    self.dfs(i, j, vis, grid, n, m)
                    islands += 1  
        return islands