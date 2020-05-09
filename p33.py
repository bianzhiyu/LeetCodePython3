from typing import *

class Solution:
    def fdP(self,n,left,right):
        if left>=right:
            return -1
        if right==left+1:
            return right if n[left]>n[right] else -1
        m=(left+right)//2
        if n[m]>n[left]:
            return self.fdP(n,m,right)
        return self.fdP(n,left,m)
    def gv(self,i):
        return self.n[ (i+self.p)% self.l]
    def gi(self,i):
        return (self.p+i)%self.l
    def bs(self,left,right,t):
        if left>right:
            return -1
        if left==right:
            return self.gi(left) if self.gv(left)==t else -1
        m=(left+right)//2
        pt=self.gv(m)
        if pt==t:
            return self.gi(m)
        return self.bs(m+1,right,t) if pt<t else self.bs(left,m-1,t)
    def search(self, nums: List[int], target: int) -> int:
        self.n=nums
        self.l=len(nums)
        if self.l==0:
            return -1
        self.p=self.fdP(nums,0,len(nums)-1)
        if self.p==-1:
            self.p=0
        return self.bs(0,len(nums)-1,target)
