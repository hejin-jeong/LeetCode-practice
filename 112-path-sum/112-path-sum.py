# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def hasPathSumHelper(node, targetSum):
            # base case: if the node is a leaf node
            if not node.left and not node.right and targetSum == node.val:
                return True
            
            # recursive case
            
            # process left tree
            if node.left and hasPathSumHelper(node.left, targetSum - node.val):
                return True
                
            # process right tree
            if node.right and hasPathSumHelper(node.right, targetSum - node.val):
                return True
            
            return False
            
        if not root:
            return False
        
        return hasPathSumHelper(root, targetSum)
        