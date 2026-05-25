class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0 
        max_area = 0 
        
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            area = 1

            area += dfs(r+1,c) #up
            area +=  dfs(r-1,c) #down
            area += dfs(r,c+1) #right
            area += dfs(r,c-1) #left

            return area

       
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    area = dfs(x,y)
                    max_area = max(area, max_area)

        return max_area
