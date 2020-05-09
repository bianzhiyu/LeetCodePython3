from typing import *

class Solution:
    def work(self,state,st,n,rml,uml,Ans):
        if st==2*n:
            Ans.append(state.decode())
            return
        if rml>0:
            state[st]=40 #ord("(")
            self.work(state,st+1,n,rml-1,uml+1,Ans)
        if uml>0:
            state[st]=41 #ord(")")
            self.work(state,st+1,n,rml,uml-1,Ans)
    def generateParenthesis(self, n: int) -> List[str]:
        Ans=[]
        state=bytearray(("a"*(2*n)).encode())
        self.work(state,0,n,n,0,Ans)
        return Ans