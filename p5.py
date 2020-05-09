from typing import *

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s=="":
            return ""
        l=len(s)
        maxlen=1
        bestl=0
        bestr=0
        for i in range(l):
            j=i-1
            k=i+1
            while j>=0 and k<l:
                if s[j]!=s[k]:
                    break
                if k-j+1>maxlen:
                    maxlen=k-j+1
                    bestl=j
                    bestr=k
                j-=1
                k+=1
            j=i
            k=i+1
            while j>=0 and k<l:
                if s[j]!=s[k]:
                    break
                if k-j+1>maxlen:
                    maxlen=k-j+1
                    bestl=j
                    bestr=k
                j-=1
                k+=1
        return s[bestl:bestr+1]

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
          
            ret = Solution().longestPalindrome(line)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()