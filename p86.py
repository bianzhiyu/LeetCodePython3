from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        bhl,bhr=ListNode(0),ListNode(0)
        pl,pr=bhl,bhr
        while head:
            if head.val<x:
                pl.next=head
                pl=pl.next
            else:
                pr.next=head
                pr=pr.next
            head=head.next
        pl.next=bhr.next
        pr.next=None
        return bhl.next