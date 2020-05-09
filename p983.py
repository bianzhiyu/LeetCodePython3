from typing import *

class Solution:
    def bs(self,a,l,r,t):
        if l>r:
            return -1
        if l==r:
            return l
        if r==l+1:
            return r if a[r]<=t else l
        m=(l+r)//2
        if a[m]<=t:
            return self.bs(a,m,r,t)
        else:
            return self.bs(a,l,m-1,t)
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        l=len(days)
        l1=list(range(l))
        l2=list(range(l))
        for i in range(l):
            if days[i]-7<days[0]:
                l1[i]=-1
            else:
                l1[i]=self.bs(days,0,i-1,days[i]-7)
            if days[i]-30<days[0]:
                l2[i]=-1
            else:
                l2[i]=self.bs(days,0,i-1,days[i]-30)
        p=[0 for i in range(l)]
        for i in range(l):
            p[i]=min((0 if i-1<0 else p[i-1])+costs[0],\
                (0 if i-l1[i]<0 else p[l1[i]])+costs[1],\
                (0 if i-l2[i]<0 else p[l2[i]])+costs[2] )
        return p[l-1]
                