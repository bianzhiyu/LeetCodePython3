from typing import *

class Solution:
    def maximalRectangle(self,mat: List[List[str]]) -> int:
        if len(mat)==0 or len(mat[0])==0:
            return 0
        m=len(mat)
        n=len(mat[0])
        dp=[[[0 for k in range(m)] for j in range(n)]  for i in range(m)]
        for x1 in range(m):
            for x2 in range(x1,m):
                if (mat[x2][n-1]!='1'):
                    for i in range(x2,m):
                        dp[x1][n-1][i]=0
                    break
                dp[x1][n-1][x2]=x2-x1+1
        for y1 in range(n-2,-1,-1):
            for x1 in range(m):
                for x2 in range(x1,m):
                    if mat[x2][y1]!='1':
                        for i in range(x2,m):
                            dp[x1][y1][i]=0
                        break
                    dp[x1][y1][x2]=dp[x1][y1+1][x2]+x2-x1+1
        ans=0
        for x1 in range(m):
            for x2 in range(m):
                for y1 in range(n):
                    if (dp[x1][y1][x2]>ans):
                        ans=dp[x1][y1][x2]
        return ans

##
mat=[["0","1"],["1","0"]]
s=Solution()
print(s.maximalRectangle(mat))


