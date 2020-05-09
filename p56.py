from typing import *

class Solution:
    def merge(self, iv: List[List[int]]) -> List[List[int]]:
        iv.sort()
        l=len(iv)
        Ans=[]
        i=0
        while i<l:
            j=i+1
            r=iv[i][1]
            while j<l and iv[j][0]<=r:
                if r<iv[j][1]:
                    r=iv[j][1]
                j+=1
            Ans.append([iv[i][0],r])
            i=j
        return Ans