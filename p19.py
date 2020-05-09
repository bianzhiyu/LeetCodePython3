from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head==None:
            return head
        l=1
        b=head
        while b.next!=None:
            b=b.next
            l+=1
        n=l+1-n
        if n==1:
            return head.next
        b=head
        for i in range(n-2):
            b=b.next
        b.next=b.next.next
        return head