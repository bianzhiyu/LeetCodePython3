from typing import *
import json

class Solution:
    def work(self,l1,l2,s1,s2,k):
        if len(l1)-s1<len(l2)-s2:
            l1,l2,s1,s2=l2,l1,s2,s1
        if (s2==len(l2)):
            return l1[s1+k-1]
        if k==1:
            return min(l1[s1],l2[s2])
        k1=min(k//2,len(l1))
        k2=min(k//2,len(l2))
        if (l1[s1+k1-1]<=l2[s2+k2-1]):
            return self.work(l1,l2,s1+k1,s2,k-k1)
        else:
            return self.work(l1,l2,s1,s2+k2,k-k2)
        

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sl=len(nums1)+len(nums2)
        if sl%2==0:
            return (self.work(nums1,nums2,0,0,sl//2)+self.work(nums1,nums2,0,0,sl//2+1))/2
        else:
            return self.work(nums1,nums2,0,0,sl//2+1)

##background

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums1 = stringToIntegerList(line)
            line = next(lines)
            nums2 = stringToIntegerList(line)
            
            ret = Solution().findMedianSortedArrays(nums1, nums2)

            out = str(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()