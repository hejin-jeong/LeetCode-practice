# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    first, second = None, None
    prev = TreeNode((-1)*float('inf'),None,None)
    
    def inorder(self, root):
        if (root==None): 
            return

        self.inorder(root.left)

        if (self.first==None and self.prev.val>root.val):
            self.first = self.prev
        if (self.first!=None and self.prev.val>root.val):
            self.second = root

        self.prev = root
        
        self.inorder(root.right)
    
    def recoverTree(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.inorder(root)
        
        temp = self.first.val
        self.first.val = self.second.val
        self.second.val = temp