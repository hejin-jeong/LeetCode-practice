# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def min_depth_helper(node, count):
            if not node.left and not node.right:
                return count

            left_depth = float('inf')
            if node.left:
                left_depth = min_depth_helper(node.left, count+1)

            right_depth = float('inf')
            if node.right:
                right_depth = min_depth_helper(node.right, count+1)

            return min(left_depth, right_depth)

        if root is None:
            return 0

        return min_depth_helper(root, 1)
        