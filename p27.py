from typing import *

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l=len(nums)
        if l==0:
            return 0
        wp=0
        for i in range(l):
            if nums[i]!=val:
                nums[wp]=nums[i]
                wp+=1
        return wp