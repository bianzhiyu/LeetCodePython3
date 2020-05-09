from typing import *

class Solution:
    def work(self,p,st,n,Ans,h1,h2,h3):
        if st==n:
            t=["" for i in range(n)]
            for i in range(n):
                for j in range(n):
                    t[i]=t[i]+("." if j!=p[i] else "Q")
            Ans.append(t)
        for i in range(n):
            if not h1[i] and not h2[st+i] and not h3[st-i]:
                h1[i]=True
                h2[st+i]=True
                h3[st-i]=True
                p[st]=i
                self.work(p,st+1,n,Ans,h1,h2,h3)
                h1[i]=False
                h2[st+i]=False
                h3[st-i]=False
    def solveNQueens(self, n: int) -> List[List[str]]:
        Ans=[]
        self.work(list(range(n)),0,n,Ans,[False for i in range(n)],[False for i in range(2*n)],[False for i in range(-n,n+1)])
        return Ans