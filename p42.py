from typing import *
import json

class Solution:
    def trap(self, h: List[int]) -> int:
        l=len(h)
        if l==0:
            return 0
        lMax=list(range(l))
        rMax=list(range(l))
        lMax[0]=0
        for i in range(1,l):
            lMax[i]=max(lMax[i-1],h[i-1])
        rMax[l-1]=0
        for i in range(l-2,-1,-1):
            rMax[i]=max(rMax[i+1],h[i+1])
        ts=0
        for i in range(l):
            ts+=max(min(lMax[i],rMax[i])-h[i],0)
        return ts

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
            height = stringToIntegerList(line)
            
            ret = Solution().trap(height)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()