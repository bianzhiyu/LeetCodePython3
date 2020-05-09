from typing import *

class Solution:
    def getA(self,s,i,j,k):
        if i==0 and j==0:
            return s[k-1][k-1]
        if i==0:
            return s[k-1][j+k-1]-s[k-1][j-1]
        if j==0:
            return s[i+k-1][k-1]-s[i-1][k-1]
        return s[i+k-1][j+k-1]+s[i-1][j-1]-s[i+k-1][j-1]-s[i-1][j+k-1]
    def maximalSquare(self, a: List[List[str]]) -> int:
        if len(a)==0 or len(a[0])==0:
            return 0
        m=len(a)
        n=len(a[0])
        s=[[0 for i in range(n)] for j in range(m)]
        s[0][0]=1 if a[0][0]=="1" else 0
        for i in range(1,m):
            s[i][0]=s[i-1][0]+(1 if a[i][0]=="1" else 0)
        for i in range(1,n):
            s[0][i]=s[0][i-1]+(1 if a[0][i]=="1" else 0)
        for i in range(1,m):
            for j in range(1,n):
                s[i][j]=s[i-1][j]+s[i][j-1]-s[i-1][j-1]+(1 if a[i][j]=="1" else 0)
        Ans=0
        for i in range(m):
            for j in range(n):
                for k in range(round(Ans**0.5)+1,min(m-i,n-j)+1):
                    a=self.getA(s,i,j,k)
                    if a==k*k:
                        Ans=k*k
                    else:
                        break
        return Ans

i=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
print(Solution().maximalSquare(i))
