from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSame(self,a,b):
        if a==None:
            return b==None
        if b==None:
            return False
        return a.val==b.val and self.isSame(a.left,b.left) and self.isSame(a.right,b.right)
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s==None:
            return t==None
        return self.isSame(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)