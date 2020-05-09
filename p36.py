from typing import *

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            u=set()
            for j in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in u:
                    return False
                u.add(board[i][j])
        for j in range(9):
            u=set()
            for i in range(9):
                if board[i][j]==".":
                    continue
                if board[i][j] in u:
                    return False
                u.add(board[i][j])
        u=[set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                g=(i//3)*3+j//3
                if board[i][j] in u[g]:
                    return False
                u[g].add(board[i][j])
        return True