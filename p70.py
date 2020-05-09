from typing import *

class Solution:
    def climbStairs(self, n: int) -> int:
        a=list(range(n+3))
        a[0],a[1]=1,1
        for i in range(2,n+1):
            a[i]=a[i-1]+a[i-2]
        return a[n]