"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
"""


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        big = set()
        for i in xrange(0, 9):
            for j in xrange(0, 9):
                if board[i][j] != '.':
                    cur = board[i][j]
                    if (i, cur) in big or (cur, j) in big or (i / 3, j / 3, cur) in big:
                        return False
                    big.add((i, cur))
                    big.add((cur, j))
                    big.add((i / 3, j / 3, cur))
        return True
