class Solution(object):
    def numIslands(self, grid):
        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(i, j, grid)
                    count += 1

        return count

    def dfs(self, row, col, grid):
        grid[row][col] = "0"

        # Up
        if row > 0 and grid[row - 1][col] == "1":
            self.dfs(row - 1, col, grid)

        # Right
        if col < len(grid[0]) - 1 and grid[row][col + 1] == "1":
            self.dfs(row, col + 1, grid)

        # Down
        if row < len(grid) - 1 and grid[row + 1][col] == "1":
            self.dfs(row + 1, col, grid)

        # Left
        if col > 0 and grid[row][col - 1] == "1":
            self.dfs(row, col - 1, grid)