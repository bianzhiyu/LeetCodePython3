from typing import *

class Solution:
    di=[[0,1],[1,0],[0,-1],[-1,0]]
    def work(self,x:int,y:int,m:int,n:int,b: List[List[str]],h:List[List[bool]],s:str,st:int)->bool:
        if st==len(s):
            return True
        for i in range(4):
            nx,ny=x+Solution.di[i][0],y+Solution.di[i][1]
            if nx>=0 and ny>=0 and nx<m and ny<n and b[nx][ny]==s[st] and not h[nx][ny]:
                h[nx][ny]=True
                if self.work(nx,ny,m,n,b,h,s,st+1):
                    return True
                h[nx][ny]=False
        return False
        
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board)==0 or len(board[0])==0:
            return False
        if len(word)==0:
            return True
        m,n=len(board),len(board[0])
        h=[[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    h[i][j]=True
                    if self.work(i,j,m,n,board,h,word,1):
                        return True
                    h[i][j]=False
        return False