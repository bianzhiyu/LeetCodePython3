from typing import *

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        l1,l2=len(s1),len(s2)
        if l1==0:
            return l2==0
        if l2==0:
            return l1==0
        if l1!=l2:
            return False
        dp=[[[False for k in range(l1+1)] for j in range(l1)] for i in range(l1)]
        for i in range(l1):
            for j in range(l2):
                dp[i][j][1]=True if s1[i]==s2[j] else False
        for k in range(2,l1+1):
            for i in range(0,l1-k+1):
                for j in range(0,l1-k+1):
                    dp[i][j][k]=False
                    for sp in range(k-1):
                        if dp[i][j][sp+1] and dp[i+sp+1][j+sp+1][k-sp-1] or dp[i][j+k-1-sp][sp+1] and dp[i+sp+1][j][k-sp-1]:
                            dp[i][j][k]=True
                            break
        return dp[0][0][l1]