from typing import *

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        canGo=0
        for i in range(len(nums)):
            if i>canGo:
                return False
            if i+nums[i]>canGo:
                canGo=i+nums[i]
        return True