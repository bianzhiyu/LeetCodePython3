from typing import *
import json

class Solution:
    def jump(self, nums: List[int]) -> int:
        l=len(nums)
        if l<=1:
            return 0
        step=0
        left=0
        right=0
        while True:
            nr=right
            for i in range(left,right+1):
                if i+nums[i]>nr:
                    nr=i+nums[i]
            if nr==right:
                return None
            if nr>=l-1:
                return step+1
            step+=1
            left=right+1
            right=nr

##background
def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            
            ret = Solution().jump(nums)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()