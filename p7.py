from typing import *

class Solution:
    def reverse(self, x: int) -> int:
        if x==0:
            return 0
        if x>0:
            flag=True
        else:
            flag=False
            x=-x
        a=[i for i in str(x)]
        a.reverse()
        x=""
        for i in a:
            x=x+i
        x=int(x)
        if flag:
            return 0 if x>2147483647 else x
        else:
            return 0 if x>2147483648 else -x


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
            
            ret = Solution().reverse(x)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()