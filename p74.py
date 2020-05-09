from typing import *

class Solution:
    def gv(self,i:int)->int:
        return self.d[i//self.s2][i%self.s2]
    def bs(self,tar:int,left:int,right:int)->bool:
        if left>right:
            return False
        if left==right:
            return self.gv(left)==tar
        m=(left+right)//2
        v=self.gv(m)
        if v==tar:
            return True
        return self.bs(tar,left,m-1) if v>tar else self.bs(tar,m+1,right)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        self.d=matrix
        self.s1=len(matrix)
        self.s2=len(matrix[0])
        return self.bs(target,0,self.s1*self.s2-1)