class Solution:
    def solveNQueens(self, n):
        res = []
        board = ['.' * n for _ in range(n)]
        cols = set()
        diag1 = set() # r - c
        diag2 = set() # r + c

        def backtrack(r):
            if r == n:
                res.append(board[:])
                return
            for c in range(n):
                if c in cols or r - c in diag1 or r + c in diag2:
                    continue
                cols.add(c)
                diag1.add(r - c)
                diag2.add(r + c)
                board[r] = '.' * c + 'Q' + '.' * (n - c - 1)
                backtrack(r + 1)
                cols.remove(c)
                diag1.remove(r - c)
                diag2.remove(r + c)

        backtrack(0)
        return res