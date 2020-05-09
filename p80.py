from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        wp,rp,l=0,0,len(nums)
        while rp<l:
            nums[wp]=nums[rp]
            rp+=1
            wp+=1
            if rp<l and nums[rp]==nums[wp-1]:
                nums[wp]=nums[rp]
                rp+=1
                wp+=1
            while rp<l and nums[rp]==nums[wp-1]:
                rp+=1
        return wp