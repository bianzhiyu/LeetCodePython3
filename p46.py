from typing import *

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i=len(nums)-1
        while i>0 and nums[i]<=nums[i-1]:
            i-=1
        if i==0:
            nums.sort()
            return
        sel=i
        i-=1
        for j in range(i+1,len(nums)):
            if nums[j]>nums[i] and nums[j]<=nums[sel]:
                sel=j
        nums[i],nums[sel]=nums[sel],nums[i]
        i=i+1
        j=len(nums)-1
        while i<j:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        c=1
        for i in range(1,n+1):
            c*=i
        Ans=[]
        Ans.append(nums[:])
        for i in range(1,c):
            self.nextPermutation(nums)
            Ans.append(nums[:])
        return Ans
