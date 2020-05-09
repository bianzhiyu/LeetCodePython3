from typing import *

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        i,lw=0,len(words)
        Ans=[]
        while i<lw:
            t,lenacc,j=words[i],len(words[i]),i+1
            while j<lw and j-i+lenacc+len(words[j])<=maxWidth:
                lenacc+=len(words[j])
                j+=1                
            if j!=i+1:
                if j<lw:
                    r=(maxWidth-lenacc)%(j-i-1)
                    d=(maxWidth-lenacc)//(j-i-1)
                    for k in range(i+1,j):
                        t=t+(" "*(d+(1 if r>0 else 0)))+words[k]
                        r-=1
                else:
                    for k in range(i+1,j):
                        t+=" "+words[k]
                    t+=" "*(maxWidth-len(t))
            else:
                t+=" "*(maxWidth-len(words[i]))
            Ans.append(t)
            i=j
        return Ans
            
##test
ws=["What","must","be","acknowledgment","shall","be"]
mw=16
Ans=Solution().fullJustify(ws,mw)
print(Ans)