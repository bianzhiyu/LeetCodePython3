from typing import *

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        ret=[]
        if target%4==0 and target//4 in d and d[target//4]>=4:
            ret.append([target//4,target//4,target//4,target//4])
        for i in d:
            if d[i]>=3 and target-3*i!=i and target-3*i in d:
                ret.append([i,i,i,target-3*i])
        for i in d:
            if d[i]>=2 and (target-2*i)%2==0 and i<(target-2*i)//2 and (target-2*i)//2 in d and d[(target-2*i)//2]>=2:
                ret.append([i,i,(target-2*i)//2,(target-2*i)//2])
        for i in d:
            if d[i]>=2:
                for j in d:
                    if j!=i and target-2*i-j>j and target-2*i-j!=i and target-2*i-j in d:
                        ret.append([i,i,j,target-i-i-j])     
        for i in d:
            for j in d:
                if j<=i:
                    continue
                for k in d:
                    if k<=j:
                        continue
                    if target-i-j-k<=k:
                        continue
                    if target-i-j-k in d:
                        ret.append([i,j,k,target-i-j-k])
        return ret


