from typing import *

class Solution:
    def sl(self,n,l,r,t):
        if l>r:
            return -1
        if l==r:
            return -1 if n[l]!=t else l
        if l+1==r:
            if n[l]==t:
                return l
            return -1 if n[r]!=t else r
        m=(l+r)//2
        if n[m]>=t:
            return self.sl(n,l,m,t)
        else:
            return self.sl(n,m+1,r,t)
    def sr(self,n,l,r,t):
        if l>r:
            return -1
        if l==r:
            return -1 if n[l]!=t else l
        if l+1==r:
            if n[r]==t:
                return r
            return -1 if n[l]!=t else l
        m=(l+r)//2
        if n[m]<=t:
            return self.sr(n,m,r,t)
        else:
            return self.sr(n,l,m-1,t)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        l=self.sl(nums,0,len(nums)-1,target)
        if l==-1:
            return [-1,-1]
        else:
            return [l,self.sr(nums,0,len(nums)-1,target)]
