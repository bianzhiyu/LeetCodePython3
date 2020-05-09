from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trav(self,root):
        if root==None:
            return True,-2200000000,2200000000
        lflag,lMax,lMin=self.trav(root.left)
        rflag,rMax,rMin=self.trav(root.right)
        return lflag and rflag and lMax<root.val and rMin>root.val,\
            rMax if root.right!=None else root.val,\
            lMin if root.left!=None else root.val
    def isValidBST(self, root: TreeNode) -> bool:
        return self.trav(root)[0]
        