from typing import *

class Solution:
    def spiralOrder(self, a: List[List[int]]) -> List[int]:
        if len(a)==0 or len(a[0])==0:
            return []
        m,n=len(a),len(a[0])
        ans=list(range(m*n))
        wp=0
        x,y=0,0
        d=[[0,1],[1,0],[0,-1],[-1,0]]
        i=0
        used=[[False for j in range(n)] for i in range(m)]
        used[0][0]=True
        ans[0]=a[0][0]
        for j in range(1,m*n):
            while True:
                nx,ny=x+d[i][0],y+d[i][1]
                if nx<0 or nx>=m or ny<0 or ny>=n or used[nx][ny]:
                    i=(i+1)%4
                else:
                    break
            x+=d[i][0]
            y+=d[i][1]
            used[x][y]=True
            ans[j]=a[x][y]
        return ans

