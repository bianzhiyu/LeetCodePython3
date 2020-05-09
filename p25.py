from typing import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasK(self,h,k):
        c=0
        while h and c<k:
            c+=1
            h=h.next
        return c>=k
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k<=1:
            return head
        bh=ListNode(0)
        p=bh
        a=list(range(k))
        while head:
            if not self.hasK(head,k):
                while head:
                    p.next=head
                    p=p.next
                    head=head.next
                break
            for i in range(k):
                a[i]=head
                head=head.next
            for i in range(k):
                p.next=a[k-1-i]
                p=p.next
            p.next=head
        return bh.next