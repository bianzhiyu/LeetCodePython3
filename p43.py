from typing import *

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1=[ord(c)-48 for c in num1]
        n1.reverse()
        n2=[ord(c)-48 for c in num2]
        n2.reverse()
        l1=len(n1)
        l2=len(n2)
        n3=[0 for i in range(l1+l2)]
        for i in range(l2):
            r=0
            for j in range(l1):
                r+=n1[j]*n2[i]+n3[i+j]
                n3[i+j]=r%10
                r=r//10
            j=l1+i
            while r>0:
                r+=n3[j]
                n3[j]=r%10
                r=r//10
        i=l1+l2-1
        while i>0 and n3[i]==0:
            i-=1
        a=""
        while i>=0:
            a=a+str(n3[i])
            i-=1
        return a

