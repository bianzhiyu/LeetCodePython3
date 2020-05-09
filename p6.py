from typing import *

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        if s=="":
            return ""
        P=2*numRows-2
        l=len(s)
        ret=list(range(l))
        wp=0
        st=0
        while st<l:
            ret[wp]=s[st]
            wp+=1
            st+=P
        for i in range(1,numRows-1):
            st=i
            while st<l:
                ret[wp]=s[st]
                wp+=1
                if st+P-2*i<l:
                    ret[wp]=s[st+P-2*i]
                    wp=wp+1
                st+=P
        st=numRows-1
        while st<l:
            ret[wp]=s[st]
            wp+=1
            st+=P
        x=""
        for i in ret:
            x=x+i
        pass
        return x

##background
def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n').strip('"')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = line
            line = next(lines)
            numRows = int(line)
            
            ret = Solution().convert(s, numRows)

            print(ret)
        except StopIteration:
            break

if __name__ == '__main__':
    main()