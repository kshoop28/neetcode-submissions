class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        column = len(board[0])

        def dfs(r, c):
            # we only want O's
            if board[r][c] != "O":
                return

            # mark as temporary (safe)
            board[r][c] = "T"

            # down
            if r + 1 < rows and board[r + 1][c] == "O":
                dfs(r + 1, c)

            # up
            if r - 1 >= 0 and board[r - 1][c] == "O":
                dfs(r - 1, c)

            # right
            if c + 1 < column and board[r][c + 1] == "O":
                dfs(r, c + 1)

            # left
            if c - 1 >= 0 and board[r][c - 1] == "O":
                dfs(r, c - 1)

        # cycling at left and right border
        for i in range(rows):
            # left border
            if board[i][0] == "O":
                dfs(i, 0)
            # right border
            if board[i][column - 1] == "O":
                dfs(i, column - 1)

        # cycling top and down border
        for i in range(column):
            # up border
            if board[0][i] == "O":
                dfs(0, i)
            # down border
            if board[rows - 1][i] == "O":
                dfs(rows - 1, i)

        # final pass: turning rest of T's back into O
        # turning rest of O's into X
        for r in range(rows):
            for c in range(column):
                if board[r][c] == "O":
                    board[r][c] = "X"   # surrounded
                elif board[r][c] == "T":
                    board[r][c] = "O"   # restore safe
