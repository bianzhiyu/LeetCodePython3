from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        bh=ListNode(0)
        p=bh
        while head:
            v=head.val
            p.next=ListNode(v)
            p=p.next
            head=head.next
            while head and head.val==v:
                head=head.next
        return bh.next