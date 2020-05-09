from typing import *

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i=len(nums)-1
        while i>0 and nums[i]<=nums[i-1]:
            i-=1
        if i==0:
            nums.sort()
            return False
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
        return True
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        Ans=[]
        Ans.append(nums[:])
        while self.nextPermutation(nums):
            Ans.append(nums[:])
        return Ans