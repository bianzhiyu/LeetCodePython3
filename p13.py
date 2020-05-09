from typing import *

class Solution:
    def romanToInt(self, s: str) -> int:
        l=len(s)
        p=0
        sum=0
        d2={"CM":900,"CD":400,"XC":90,"XL":40,"IX":9,"IV":4}
        d1={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
        while p<l:
            if p<l-1:
                t=s[p:p+2]
                if t in d2:
                    p+=2
                    sum+=d2[t]
                    continue
            sum+=d1[s[p]]
            p+=1
        return sum
            

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
            
            ret = Solution().romanToInt(line)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()