from typing import *

class MDir:
    def __init__(self,name,par:object,prop=0):
        self.name=name
        self.subDir={}
        self.parDir=par
        self.prop=prop # if prop%2==1: is root
class Solution:
    def genPath(self,r:MDir)->str:
        return "" if r.prop%2==1 else self.genPath(r.parDir)+"/"+r.name
    def simplifyPath(self, path: str) -> str:
        while path.find("//")!=-1:
            path=path.replace("//","/")
        l=len(path)
        i=1
        Rt=MDir("/",None,1)
        while i<l:
            nextdelim=path.find("/",i)
            if nextdelim==-1:
                name=path[i:]
                i=l
            else:
                name=path[i:nextdelim]
                i=nextdelim+1
            if name==".":
                continue
            if name=="..":
                Rt=Rt.parDir if Rt.prop%2==0 else Rt
                continue
            if name not in Rt.subDir:
                Rt.subDir[name]=MDir(name,Rt,0)
            Rt=Rt.subDir[name]
        return "/" if Rt.prop%2==1 else self.genPath(Rt)
        
##test
S=Solution()
print(S.simplifyPath("/home//foo/"))