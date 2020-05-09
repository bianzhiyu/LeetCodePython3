from typing import *

class Solution:
    def plusOne(self, d: List[int]) -> List[int]:
        d=d[:]
        d[-1]+=1
        for i in range(len(d)-1,0,-1):
            d[i-1]+=d[i]//10
            d[i]%=10
        if d[0]<10:
            return d
        d.insert(0,1)
        d[1]%=10
        return d