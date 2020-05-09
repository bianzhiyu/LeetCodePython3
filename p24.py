from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        bh=ListNode(0)
        p=bh
        while head:
            if not head.next:
                p.next=head
                break
            q1=head
            q2=q1.next
            head=head.next.next
            p.next,q2.next,q1.next=q2,q1,q2.next
            p=p.next.next
        return bh.next