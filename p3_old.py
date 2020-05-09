from typing import *

class SolutionOld:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=0
        ed=0
        L=len(s)
        a=set()
        ans=0
        while (ed<L):
            if s[ed] in a:
                while (s[ed] in a):
                    a.remove(s[st])
                    st+=1
            else:
                a.add(s[ed])
                ed+=1
                if ed-st>ans:
                    ans=ed-st
        return ans