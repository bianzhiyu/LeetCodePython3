class Solution:
    def countAndSay(self, n: int) -> str:
        s="1"
        if n==1:
            return s
        for i in range(2,n+1):
            ns=""
            j=0
            ls=len(s)
            while j<ls:
                k=j+1
                while k<ls and s[k]==s[j]:
                    k+=1
                ns=ns+str(k-j)+s[j]
                j=k
            s=ns
        return s