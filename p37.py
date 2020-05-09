from typing import *

class Solution:
    def __init__(self,*l,**d):
        self.g=[[0,0,0,1,1,1,2,2,2],\
            [0,0,0,1,1,1,2,2,2],\
            [0,0,0,1,1,1,2,2,2],\
            [3,3,3,4,4,4,5,5,5],\
            [3,3,3,4,4,4,5,5,5],\
            [3,3,3,4,4,4,5,5,5],\
            [6,6,6,7,7,7,8,8,8],\
            [6,6,6,7,7,7,8,8,8],\
            [6,6,6,7,7,7,8,8,8]]
        self.row=[[False for j in range(9)] for i in range(9)]
        self.col=[[False for j in range(9)] for i in range(9)]
        self.blk=[[False for j in range(9)] for i in range(9)]
    def work(self,st,board):
        if st==self.workLen:
            return True
        x=self.toSolve[st][0]
        y=self.toSolve[st][1]
        for i in range(9):
            if not self.row[x][i] and not self.col[y][i] and not self.blk[self.g[x][y]][i]:
                self.row[x][i]=True
                self.col[y][i]=True
                self.blk[self.g[x][y]][i]=True
                
                if self.work(st+1,board):
                    board[x][y]=str(i+1)
                    return True
                self.row[x][i]=False
                self.col[y][i]=False
                self.blk[self.g[x][y]][i]=False
        return False
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.toSolve=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    self.toSolve.append([i,j])
                else:
                    c=ord(board[i][j])-49
                    self.row[i][c]=True
                    self.col[j][c]=True
                    self.blk[self.g[i][j]][c]=True
        self.workLen=len(self.toSolve)
        self.work(0,board)
