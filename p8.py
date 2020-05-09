from typing import *

class Solution:
    def myAtoi(self, s: str) -> int:
        l=len(s)
        p=0
        while p<l and s[p]==" ":
            p+=1
        if p==l:
            return 0
        flag=True
        if s[p]=="+" or s[p]=="-":
            flag=True if s[p]=="+" else False
            p=p+1
        if p==l:
            return 0
        c=ord(s[p])
        if c<48 or c>57:
            return 0
        n=0
        for c in [ ord(i)-48 for i in s[p:]]:
            if c<0 or c>9:
                break
            n=n*10+c
        if flag:
            return n if n<=2147483647 else 2147483647
        else:
            return -n if n<=2147483648 else -2147483648
        
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
            
            ret = Solution().myAtoi(line)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()