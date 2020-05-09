from typing import *

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1)*len(word2)==0:
            return max(len(word1),len(word2))
        l1,l2=len(word1),len(word2)
        d=[[0 for j in range(l2+1)] for i in range(l1+1)]
        d[0]=[j for j in range(l2+1)]
        for i in range(1,l1+1):
            d[i][0]=i
            for j in range(1,l2+1):
                d[i][j]=min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+(0 if word1[i-1]==word2[j-1] else 1))
        return d[l1][l2]