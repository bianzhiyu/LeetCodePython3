from typing import *

class Solution:
    def work(self,n,left,right,t):
        if left==right:
            if t==n[left]:
                return left
            return left if t<=n[left] else left+1
        if left+1==right:
            if t>n[right]:
                return right+1
            if t<=n[left]:
                return left
            return right
        m=(left+right)//2
        if n[m]==t:
            return m
        if n[m]>t:
            return self.work(n,left,m-1,t)
        return self.work(n,m+1,right,t)
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return 0
        return self.work(nums,0,len(nums)-1,target)

