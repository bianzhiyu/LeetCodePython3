from typing import *

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m,n=m-1,n-1
        if m>n:
            m,n=m+n,n
        else:
            m,n=m+n,m
        Ans=1
        div=2
        for i in range(m-n+1,m+1):
            Ans*=i
            if div<=n and Ans%div==0:
                Ans//=div
                div+=1
        return Ans