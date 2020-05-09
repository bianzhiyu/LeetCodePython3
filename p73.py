from typing import *

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if len(matrix)==0 or len(matrix[0])==0:
            return 
        m,n=len(matrix),len(matrix[0])
        h1=[False for i in range(m)]
        h2=[False for i in range(n)]
        s1,s2=set(),set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    h1[i],h2[j]=True,True
        for i in range(m):
            for j in range(n):
                if h1[i] or h2[j]:
                    matrix[i][j]=0
