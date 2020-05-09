from typing import *

class Solution:
    def intv(self,a:List[int],b:List[int])->bool:
        return not( a[1]<b[0] or a[0]>b[1])
    def insert(self, iv: List[List[int]], ni: List[int]) -> List[List[int]]:
        Ans=[]
        l=len(iv)
        for i in range(l):
            if not self.intv(iv[i],ni):
                Ans.append(iv[i][:])
            else:
                t=[min(ni[0],iv[i][0]),max(ni[1],iv[i][1])]
                j=i+1
                while j<l and self.intv(iv[j],t):
                    t[1]=max(t[1],iv[j][1])
                    j+=1
                Ans.append(t)
                for k in range(j,l):
                    Ans.append(iv[k][:])
                return Ans
        Ans.append(ni)
        Ans.sort()
        return Ans

##
iv=[[1,3],[6,9]]
ni=[2,5]
n=Solution().insert(iv,ni)
print(n)