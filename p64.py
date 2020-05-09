from typing import *

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n=len(grid),len(grid[0])
        d=[[0 for j in range(n)] for i in range(m)]
        d[0][0]=grid[0][0]
        for i in range(1,m):
            d[i][0]=grid[i][0]+d[i-1][0]
        for i in range(1,n):
            d[0][i]=grid[0][i]+d[0][i-1]
        for i in range(1,m):
            for j in range(1,n):
                d[i][j]=grid[i][j]+(d[i-1][j] if d[i-1][j]<d[i][j-1] else d[i][j-1])
        return d[m-1][n-1]