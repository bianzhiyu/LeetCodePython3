from typing import *
import json

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=len(nums)
        if l==0:
            return 0
        partSum=list(range(l))
        tmp=0
        for i in range(l):
            tmp+=nums[i]
            partSum[i]=tmp
        lMinPS=list(range(l))
        lMinPS[0]=0 
        for i in range(1,l):
            lMinPS[i]=partSum[i-1] if partSum[i-1]<lMinPS[i-1] else lMinPS[i-1]
        maxAns=nums[0]
        for i in range(1,l):
            tmp=partSum[i]-lMinPS[i]
            if tmp>maxAns:
                maxAns=tmp
        return maxAns

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
            nums = stringToIntegerList(line)
            
            ret = Solution().maxSubArray(nums)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()