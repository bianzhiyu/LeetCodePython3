class Solution:
    def getNext(self,p):
        l=len(p)
        n=list(range(l))
        n[0]=0
        if (l>1):
            n[1]=0
        for i in range(2,l):
            y=n[i-1]
            while y>0 and p[i-1]!=p[y]:
                y=n[y]
            if p[i-1]==p[y]:
                n[i]=y+1
            else:
                n[i]=0
        return n
            
    def strStr(self, s: str, pattern: str) -> int:
        lp=len(pattern)
        ls=len(s)
        if lp==0:
            return 0
        if ls==0:
            return -1
        n=self.getNext(pattern)
        i=0
        j=0
        while i<=ls:
            if j==lp:
                return i-lp
            if i==ls:
                return -1
            if (s[i]==pattern[j]):
                i+=1
                j+=1
            elif j<=0:
                i+=1
                j=0
            else:
                j=n[j]
        return -1