from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        ans=[]
        if 0 in d and d[0]>=3:
            ans.append([0,0,0])
        ans.extend([i,i,-2*i] for i in d if i!=0 and d[i]>=2 and -2*i in d)
        vals=[i for i in d]
        vals.sort()
        l=len(vals)
        for i in range(l):
            for j in range(i+1,l):
                if -vals[i]-vals[j]>vals[j] and -vals[i]-vals[j] in d:
                    ans.append([vals[i],vals[j],-vals[i]-vals[j]])
        return ans


