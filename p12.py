from typing import *

class Solution:
    def rd(self,unit,num,ten,five,one,s):
        s=s+ten*(num//(10*unit))
        num=num%(10*unit)
        if (num>=9*unit):
            num-=9*unit
            s=s+one+ten
        if (num>=5*unit):
            num-=5*unit
            s=s+five
        if (num>=4*unit):
            num-=4*unit
            s=s+one+five
        s=s+one*(num//unit)
        num=num%unit
        return num,s

    def intToRoman(self, num: int) -> str:
        if num==0:
            return ""
        num,s=self.rd(100,num,"M","D","C","")
        num,s=self.rd(10,num,"C","L","X",s)
        nums,s=self.rd(1,num,"X","V","I",s)
        return s

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
            num = int(line)
            
            ret = Solution().intToRoman(num)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
        