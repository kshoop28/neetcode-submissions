class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        column = len(board[0])
        
        def dfs(row,col):

            if row < 0 or col < 0 or row >= rows or col >= column:
                return
            
            # we only want O's
            if board[row][col] != "O":
                return

            board[row][col] = "T"

            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)



        #cycling at left and right border
        for i in range(rows):
            #left border
            if board[i][0] == "O":
                dfs(i,0)
            #right border
            if board[i][column-1] == "O":
                dfs(i,column-1)

        #cycling top and down border
        for i in range(column):
            #up border
            if board[0][i] == "O":
                dfs(0,i)
            #down border
            if board[rows-1][i] == "O":
                dfs(rows-1,i)
        

        # final pass: turning rest of T's back into O
        # turning rest of O's into X
        for r in range(rows):
            for c in range(column):
                if board[r][c] == "O":
                    board[r][c] = "X"   # surrounded
                elif board[r][c] == "T":
                    board[r][c] = "O"   # restore safe

       




