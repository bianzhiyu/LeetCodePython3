from typing import *

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        d=[0,0,0]
        for i in nums:
            d[i]+=1
        wp=0
        for i in range(3):
            for j in range(d[i]):
                nums[wp]=i
                wp+=1