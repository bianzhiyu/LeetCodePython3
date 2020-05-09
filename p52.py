from typing import *

class Solution:
    def work(self,st,n,h1,h2,h3):
        if st==n:
            self.Ans+=1
            return
        for i in range(n):
            if not h1[i] and not h2[st+i] and not h3[st-i]:
                h1[i]=True
                h2[st+i]=True
                h3[st-i]=True
                self.work(st+1,n,h1,h2,h3)
                h1[i]=False
                h2[st+i]=False
                h3[st-i]=False
    def totalNQueens(self, n: int) -> int:
        self.Ans=0
        self.work(0,n,[False for i in range(n)],[False for i in range(2*n)],[False for i in range(-n,n+1)])
        return self.Ans
