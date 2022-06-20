# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
       
        return self.isBalancedHelper(root) != -1
    
    def isBalancedHelper(self, root):
        if root is None:
            return 0
        
        left = self.isBalancedHelper(root.left)
        right = self.isBalancedHelper(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

        
#     def isBalanced(self, root):
            
#         def check(root):
#             if root is None:
#                 return 0
#             left  = check(root.left)
#             right = check(root.right)
#             if left == -1 or right == -1 or abs(left - right) > 1:
#                 return -1
#             return 1 + max(left, right)
            
#         return check(root) != -1