from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        p=head
        l=0
        while p:
            l+=1
            p=p.next
        if l==0:
            return head
        k=k%l
        if k==0:
            return head
        p=head
        for i in range(l-k):
            p=p.next
        bh=ListNode(0)
        bh.next=p
        while p.next:
            p=p.next
        p.next=head
        for i in range(l-k):
            p=p.next
        p.next=None
        return bh.next


##
