from typing import *

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans=[[0 for j in range(n)] for i in range(n)]
        wp=0
        x,y=0,0
        d=[[0,1],[1,0],[0,-1],[-1,0]]
        i=0
        used=[[False for j in range(n)] for i in range(n)]
        used[0][0]=True
        ans[0][0]=1
        for j in range(1,n*n):
            while True:
                nx,ny=x+d[i][0],y+d[i][1]
                if nx<0 or nx>=n or ny<0 or ny>=n or used[nx][ny]:
                    i=(i+1)%4
                else:
                    break
            x+=d[i][0]
            y+=d[i][1]
            used[x][y]=True
            ans[x][y]=j+1
        return ans
