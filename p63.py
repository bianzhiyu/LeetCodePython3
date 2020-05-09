from typing import *

class Solution:
    def uniquePathsWithObstacles(self, ob: List[List[int]]) -> int:
        m,n=len(ob),len(ob[0])
        d=[[0 for j in range(n)] for i in range(m)]
        d[0][0]=1 if ob[0][0]==0 else 0
        for i in range(1,m):
            d[i][0]=d[i-1][0] if ob[i][0]==0 else 0
        for i in range(1,n):
            d[0][i]=d[0][i-1] if ob[0][i]==0 else 0
        for i in range(1,m):
            for j in range(1,n):
                d[i][j]=d[i-1][j]+d[i][j-1] if ob[i][j]==0 else 0
        return d[m-1][n-1]