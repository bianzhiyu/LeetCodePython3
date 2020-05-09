from typing import *

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ft=[0 for i in range(n+2)]
        ft[0]=1
        for i in range(1,n+1):
            ft[i]=i*ft[i-1]
        a=list(range(n))
        v=[i+1 for i in range(n)]
        for i in range(n):
            x=(k-1)//ft[n-i-1]+1
            a[i]=v[x-1]
            v.pop(x-1)
            k-=x*ft[n-i-1]
        r=""
        for i in a:
            r+=str(i)
        return r

##
a=Solution().getPermutation(4,9)
print(a)