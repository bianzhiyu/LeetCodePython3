from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1:
            return strs[0]
        ml=min(len(i) for i in strs)
        if ml==0:
            return ""
        for i in range(0,ml):
            flag=True
            for j in range(1,len(strs)):
                if strs[j][i]!=strs[0][i]:
                    flag=False
                    break
            if not flag:
                break
        return strs[0][0:ml] if flag else strs[0][0:i]
