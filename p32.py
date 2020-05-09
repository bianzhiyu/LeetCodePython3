from typing import *

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)==0:
            return 0
        ml=[0 for c in s]
        for i in range(1,len(s)):
            if s[i]=="(":
                ml[i]=0
                continue
            if s[i-1]=="(":
                if i>=2 and ml[i-2]>0:
                    ml[i]=2+ml[i-2]
                else:
                    ml[i]=2
                continue
            l=ml[i-1]
            if l>0 and i-l>0 and s[i-l-1]=="(":
                if i-l>1:
                    ml[i]=l+2+ml[i-l-2]
                else:
                    ml[i]=l+2
            else:
                ml[i]=0
        return max(ml)

print(Solution().longestValidParentheses("()(())"))