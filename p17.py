from typing import *

class Solution:
    def work(self,s,Ans,r,st,ln,state):
        if st==ln:
            Ans.append(state.decode())
            return
        for c in r[s[st]]:
            state[st]=c
            self.work(s,Ans,r,st+1,ln,state)
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        r={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        rl={}
        for k in r:
            rl[k]=[ord(c) for c in r[k]]
        Ans=[]
        self.work(digits,Ans,rl,0,len(digits),bytearray(digits,"utf-8"))
        return Ans


