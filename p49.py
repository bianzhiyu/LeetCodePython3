from typing import *

class Solution:
    def parse(self,s:str):
        a=[0 for i in range(26)]
        for c in s:
            a[ord(c)-97]+=1
        return tuple(a)
    def equ(self,a,b):
        for i in range(26):
            if a[0][i]!=b[0][i]:
                return False
        return True
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a=[[self.parse(strs[i]),i] for i in range(len(strs))]
        a.sort()
        i=0
        l=len(a)
        Ans=[]
        while i<l:
            j=i+1
            t=[strs[a[i][1]]]
            while j<l and self.equ(a[j],a[i]):
                t.append(strs[a[j][1]])
                j+=1
            i=j
            Ans.append(t)
        return Ans
                
