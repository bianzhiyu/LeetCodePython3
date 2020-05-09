from typing import *

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=2200000000
        d=2200000000
        l=len(nums)
        for i in range(l-2):
            j=i+1
            k=l-1
            nt=target-nums[i]
            while j<k:
                if abs(nums[j]+nums[k]-nt)<d:
                    d=abs(nums[j]+nums[k]-nt)
                    ans=nums[i]+nums[j]+nums[k]
                if nums[j]+nums[k]==nt:
                    return target
                if nums[j]+nums[k]>nt:
                    k-=1
                else:
                    j+=1
        return ans