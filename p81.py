from typing import *

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        try:
            nums.index(target)
        except:
            return False
        else:
            return True