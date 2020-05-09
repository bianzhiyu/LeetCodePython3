from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=len(nums)
        if l==0:
            return 0
        rp=0
        wp=0
        while rp<l:
            j=rp+1
            while j<l and nums[j]==nums[rp]:
                j+=1
            nums[wp]=nums[rp]
            rp=j
            wp+=1
        return wp