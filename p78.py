from typing import *

class Solution:
    def work(self,st:int,state:List[bool],nums:List[int],Ans:List[List[int]],l:int)->None:
        if st==l:
            Ans.append([nums[i] for i in range(l) if state[i]])
            return
        state[st]=False
        self.work(st+1,state,nums,Ans,l)
        state[st]=True
        self.work(st+1,state,nums,Ans,l)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        Ans=[]
        self.work(0,list(range(len(nums))),nums,Ans,len(nums))
        return Ans
