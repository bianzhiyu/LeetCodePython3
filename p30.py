from typing import *

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if s=="" or len(words)==0 or len(words[0])==0:
            return []
        ls=len(s)
        wn=len(words)
        lw=len(words[0])
        uw=list(set(words))
        luw=len(uw)
        d={}
        for i in range(luw):
            d[uw[i]]=[0,i]
        for i in words:
            d[i][0]+=1
        ct=uw[:]
        for i in d:
            j=d[i]
            ct[j[1]]=j[0]
        mt=list(range(ls-lw+1))
        for i in range(ls-lw+1):
            tmp=s[i:i+lw]
            mt[i]=d[tmp][1]  if tmp in d else -1
        Ans=[]
        for i in range(ls-lw*wn+1):
            used=[0 for j in range(luw)]
            flag=True
            for j in range(wn):
                k=i+j*lw
                if mt[k]==-1:
                    flag=False
                    break
                k=mt[k]
                if used[k]==ct[k]:
                    flag=False
                    break
                used[k]+=1
            if flag:
                Ans.append(i)
        return Ans

