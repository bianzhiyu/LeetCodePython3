from typing import *

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ls=len(s)
        lp=len(p)
        d=[[False for j in range(ls+1)] for i in range(lp+1)]
        d[0][0]=True
        for i in range(1,lp+1):
            if p[i-1]=="?":
                for j in range(1,ls+1):
                    d[i][j]=d[i-1][j-1]
            elif p[i-1]=="*":
                for j in range(0,ls+1):
                    if d[i-1][j]:
                        for k in range(j,ls+1):
                            d[i][k]=True
                        break
            else:
                for j in range(1,ls+1):
                    d[i][j]=d[i-1][j-1] and p[i-1]==s[j-1]
        return d[lp][ls]