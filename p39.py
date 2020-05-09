from typing import *

class Solution:
    def work(self,n,st,ct,rem,Ans):
        if st==len(ct):
            if rem==0:
                t=[]
                for i in range(len(ct)):
                    for j in range(ct[i]):
                        t.append(n[i])
                Ans.append(t)
            return
        ct[st]=0
        while (rem>=0):
            self.work(n,st+1,ct,rem,Ans)
            ct[st]+=1
            rem-=n[st]
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ct=[0 for i in candidates]
        Ans=[]
        self.work(candidates,0,ct,target,Ans)
        return Ans