from typing import *

class Solution:
    def firstMissingPositive(self, a: List[int]) -> int:
        n=len(a)
        for i in range(n):
            while True:
                v=a[i]
                if v<1 or v>n:
                    break
                if a[v-1]!=v:
                    a[i],a[v-1]=a[v-1],a[i]
                else:
                    break
        for i in range(n):
            if a[i]!=i+1:
                return i+1
        return n+1