from typing import *

class Solution:
    def divide(self, a: int, b: int) -> int:
        if b<0:
            a=-a
            b=-b
        flag=True if a>=0 else False
        a=-a if a<0 else a
        if a<b:
            return 0
        l=list(range(70))
        tb=b
        l[0]=b
        m=1
        while tb+tb<=a:
            l[m]=tb+tb
            tb+=tb
            m+=1
        c=list(range(70))
        ans=0
        for i in range(m-1,-1,-1):
            if a>=l[i]:
                a-=l[i]
                c[i]=1
            else:
                c[i]=0
        tb=1
        for i in range(m):
            if c[i]==1:
                ans+=tb
            tb+=tb
        if flag:
            return ans if ans<=2147483647 else 2147483647
        else:
            return -ans if ans<=2147483648 else -2147483648

