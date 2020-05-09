from typing import *

class Solution:
    def parse(self,s:str)->List[int]:
        p=[0 for i in range(256)]
        for c in s:
            p[ord(c)]+=1
        return p
    def minWindow(self, s: str, t: str) -> str:
        pt=self.parse(t)
        ct=[0 for i in range(256)]
        dem=len([c for c in pt if c>0])
        left,right=0,0
        ls=len(s)
        AnsLeft=0
        AnsLen=2200000000
        while right<ls:
            while dem>0 and right<ls:
                x=ord(s[right])
                ct[x]+=1
                if ct[x]==pt[x]:
                    dem-=1
                right+=1
            if dem>0:
                break
            while left<right and dem==0:
                if right-left<AnsLen:
                    AnsLeft=left
                    AnsLen=right-left
                x=ord(s[left])
                ct[x]-=1
                if ct[x]==pt[x]-1:
                    dem+=1
                left+=1
        return s[AnsLeft:AnsLeft+AnsLen] if AnsLen<2000000000 else ""

