import heapq
from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, ol: List[ListNode]) -> ListNode:
        lists=[(ol[i].val,i,ol[i]) for i in range(len(ol)) if ol[i]]
        heapq.heapify(lists)
        bh=ListNode(0)
        p=bh
        while lists:
            l=heapq.heappop(lists)
            p.next=ListNode(l[0])
            p=p.next
            if l[2].next:
                heapq.heappush(lists,(l[2].next.val,l[1],l[2].next))
        return bh.next