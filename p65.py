from typing import *

class Solution:
    def isNumber(self, s: str) -> bool:
        ns = set(c for c in "0123456789")
        s=s.strip()
        if s=="":
            return False
        if s[0]=="-" or s[0]=="+":
            s=s[1:]
        if s=="":
            return False
        i=0
        while i<len(s) and s[i] in ns:
            i+=1
        if i>0:
            s=s[i:]
            if s.strip()=="":
                return True
            if s[0]==".":
                s=s[1:]
            if s.strip()=="":
                return True
            while s!="" and s[0] in ns:
                s=s[1:]
            if s.strip()=="":
                return True
        elif s[0]=='.':
            if len(s)==1 or s[1] not in ns:
                return False
            s=s[1:]
            while s!="" and s[0] in ns:
                s=s[1:]
            if s.strip()=="":
                return True
        else:
            return False
        if len(s)!=0 and s[0]!='e' and s[0]!='E':
            return False
        s=s[1:]
        if len(s)>0 and (s[0]=='+' or s[0]=='-'):
            s=s[1:]
        i=0
        while i<len(s) and s[i] in ns:
            i+=1
        if i==0:
            return False
        s=s[i:]
        return s.strip()==""


##
s="2e0"
a=Solution().isNumber(s)
print(a)
