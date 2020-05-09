from typing import *

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        a=[i for i in str(x)]
        b=a[:]
        b.reverse()
        for i in range(len(a)):
            if a[i]!=b[i]:
                return False
        return True

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
            x = int(line)
            
            ret = Solution().isPalindrome(x)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()