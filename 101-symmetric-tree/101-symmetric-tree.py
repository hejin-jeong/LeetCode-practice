# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        return self.isSymmetricHelper(root.left, root.right)
    
    
    def isSymmetricHelper(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        
        if left.val == right.val:
            outter = self.isSymmetricHelper(left.left, right.right)
            inner = self.isSymmetricHelper(left.right, right.left)
            if outter and inner:
                return True
        
        return False