from typing import *

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s=int(a,base=2)+int(b,base=2)
        if s==0:
            return "0"
        r=""
        while s>0:
            r=str(s%2)+r
            s//=2
        return r