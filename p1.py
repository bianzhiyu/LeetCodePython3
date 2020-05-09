from typing import List 
import json

class Solution:
    @staticmethod
    def bs(l,left,right,v):
        if (left>right):
            return -1
        m=(left+right)//2
        if (l[m][0]==v):
            return m
        if (l[m][0]>v):
            return Solution.bs(l,left,m-1,v)
        return Solution.bs(l,m+1,right,v)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L=len(nums)
        Arr=[[nums[i],i] for i in range(L)]
        Arr.sort()
        for i in range(L):
            j=Solution.bs(Arr,i+1,L-1,target-Arr[i][0])
            if j!=-1:
                return [Arr[i][1],Arr[j][1]]


#########################background
def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            nums = stringToIntegerList(line)
            line = next(lines)
            target = int(line)
            
            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()