from typing import *
import json

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        rem=0
        bh=ListNode(0)
        p=bh
        while (l1!=None or l2!=None):
            if l1!=None:
                rem+=l1.val
                l1=l1.next
            if l2!=None:
                rem+=l2.val
                l2=l2.next
            p.next=ListNode(rem%10)
            p=p.next
            rem=rem//10
        while (rem>0):
            p.next=ListNode(rem%10)
            p=p.next
            rem=rem//10
        return bh.next

#########################background
def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

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
            l1 = stringToListNode(line)
            line = next(lines)
            l2 = stringToListNode(line)
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
