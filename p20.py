from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
        sk=[]
        d={")":"(","]":"[","}":"{"}
        for c in s:
            if c in {"(","[","{"}:
                sk.append(c)
            elif not sk:
                return False
            elif sk.pop()!=d[c]:
                return False
        return not sk
