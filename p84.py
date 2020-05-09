from typing import *

class Solution:
    def largestRectangleArea(self, h: List[int]) -> int:
        Ans=0
        l=len(h)
        if l==0:
            return 0
        for i in range(l):
            if h[i]==0:
                continue
            nl=Ans//h[i]
            if i+nl>=l:
                continue
            th=h[i]
            for j in range(i+1,i+nl):
                if h[j]<th:
                    th=h[j]
            for j in range(i+nl,l):
                if h[j]<th:
                    th=h[j]
                ta=th*(j-i+1)
                if ta>Ans:
                    Ans=ta
                if th*(l-i)<=Ans:
                    break
        return Ans