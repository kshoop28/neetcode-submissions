class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights) #our y
        column = len(heights[0]) # our x
        curr_height = 0

        atl = set()
        pac = set()

        def dfs(r, c, visited):

            if (r, c) in visited:
                return
            visited.add((r, c))

            # down (top border)
            if r + 1 < rows and heights[r + 1][c] >= heights[r][c]:
                dfs(r + 1, c, visited)

            # up (bottom border)
            if r - 1 >= 0 and heights[r - 1][c] >= heights[r][c]:
                dfs(r - 1, c, visited)

            # right (left border)
            if c + 1 < column and heights[r][c + 1] >= heights[r][c]:
                dfs(r, c + 1, visited)

            # left (right border)
            if c - 1 >= 0 and heights[r][c - 1] >= heights[r][c]:
                dfs(r, c - 1, visited)


        # we run 4 loops for the border.
        #left border
        for row in range(0,rows):
            dfs(row,0,pac)
        #top border
        for col in range(0,column):
            dfs(0,col,pac)
        #right border
        for row in range(0,rows):
            dfs(row,column-1,atl)
        #bottom border
        for col in range(0,column):
            dfs(rows-1,col,atl)
        
        res = []
        for r in range(rows):
            for c in range(column):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res












