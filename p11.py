from typing import *
import json

class Solution:
    def maxArea(self, h: List[int]) -> int:
        l=len(h)
        if l==0:
            return 0
        left=0
        right=l-1
        Ans=0
        while left<=right:
            na=min(h[right],h[left])*(right-left)
            if na>Ans:
                Ans=na
            if (h[right]<h[left]):
                right-=1
            else:
                left+=1
        return Ans


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
            
            ret = Solution().maxArea(height)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()