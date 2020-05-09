from typing import *

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        lens=len(s)
        lenp=len(p)
        dp=[[False for j in range(lens+1)] for i in range(lenp+1)]
        dp[0][0]=True
        for i in range(1,lenp+1):
            if (p[i-1]=="."):
                for j in range(1,lens+1):
                    dp[i][j]=dp[i-1][j-1]
            elif p[i-1]=="*":
                if i==1:
                    dp[1][0]=True
                    for j in range(1,lens+1):
                        dp[i][j]=False
                    continue
                if p[i-2]==".":
                    for j in range(lens+1):
                        dp[i][j]=dp[i-2][j] or j>=1 and dp[i-1][j-1] or j>=1 and dp[i][j-1] #0, 1, >=2 times of "."
                    continue
                for j in range(lens+1):
                    dp[i][j]=dp[i-2][j] or dp[i-1][j] or j>=1 and dp[i-1][j-1] and s[j-1]==p[i-2] #0, 1, >=2 times of p[i-2]
            else:
                for j in range(1,lens+1):
                    dp[i][j]=dp[i-1][j-1] and s[j-1]==p[i-1]
        return dp[lenp][lens]

##background

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n').strip('"')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            s = line
            line = next(lines)
            p = line
            
            ret = Solution().isMatch(s, p)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()