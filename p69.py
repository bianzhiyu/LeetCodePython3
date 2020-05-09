from typing import *

class Solution:
    def mySqrt(self, x: int) -> int:
        if x<=1:
            return x
        l,r=1,x
        while l<r:
            if l+1==r:
                return r if r*r<=x else l
            m=(l+r)//2
            if m*m<=x:
                l=m
            else:
                r=m
        return l