# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return root
        
        p = root
        
        if p.left or p.right:
            temp = p.left
            p.left = p.right
            p.right = temp
            if p.left:
                self.invertTree(p.left)
            if p.right:
                self.invertTree(p.right)
            
        return root
        
        
    def invertTreeHelper(root):
        p = root
        
        if p.left or p.right:
            temp = p.left
            p.left = p.right
            p.right = temp
            if p.left:
                invertTreeHelper(p.left)
            if p.right:
                invertTreeHelper(p.right)
            
            
        