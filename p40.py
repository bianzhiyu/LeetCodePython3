from typing import *

class Solution:
    def parse(self,n:List[int]):
        k=set(n)
        d={}
        for i in k:
            d[i]=0
        for i in n:
            d[i]+=1
        return [[k,d[k]] for k in d]
    def work(self,st:int ,u:List[int],a:List[List[int]],rem:int,Ans:List[List[int]]):
        if st==len(a):
            if rem==0:
                t=[]
                for i in range(len(u)):
                    for j in range(u[i]):
                        t.append(a[i][0])
                Ans.append(t)
            return
        u[st]=0
        self.work(st+1,u,a,rem,Ans)
        for i in range(a[st][1]):
            if rem<a[st][0]:
                break
            rem-=a[st][0]
            u[st]+=1
            self.work(st+1,u,a,rem,Ans)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        a=self.parse(candidates)
        u=[0 for i in candidates]
        Ans=[]
        self.work(0,u,a,target,Ans)
        return Ans