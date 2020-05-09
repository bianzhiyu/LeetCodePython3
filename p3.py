from typing import *

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=0
        a=set()
        ans=0
        for ed in range(len(s)):
            while (s[ed] in a):
                a.remove(s[st])
                st+=1
            a.add(s[ed])
            if ed-st+1>ans:
                ans=ed-st+1
        return ans

##background
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
            
            ret = Solution().lengthOfLongestSubstring(line)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()