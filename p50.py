from typing import *

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if x==0 or x==1:
            return x
        if n<0:
            x=1/x
            n=-n
        b=[]
        while n>0:
            b.append(n%2)
            n=n//2
        a=1
        for c in b:
            if c==1:
                a*=x
            x*=x
        return a

print(Solution().myPow(2,10))