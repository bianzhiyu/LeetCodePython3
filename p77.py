from typing import *

class Solution:
    def work(self,n:int,k:int,st:int,start:int,state:List[int],Ans:List[List[int]])->None:
        if st==k:
            Ans.append(state[:])
            return
        for i in range(start,n+2+st-k):
            state[st]=i
            self.work(n,k,st+1,i+1,state,Ans)
    def combine(self, n: int, k: int) -> List[List[int]]:
        Ans=[]
        self.work(n,k,0,1,list(range(k)),Ans)
        return Ans