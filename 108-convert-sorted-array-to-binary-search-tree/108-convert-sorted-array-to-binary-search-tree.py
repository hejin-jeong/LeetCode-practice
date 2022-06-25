# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def create_bst_helper(nums):
            if not nums:
                return None

            if len(nums) == 1:
                return TreeNode(nums[0], None, None)

            middle = len(nums)//2
            # if middle < len(nums):
            current = TreeNode(nums[middle], None, None)

            left_subtree = create_bst_helper(nums[:middle]) 
            right_subtree = create_bst_helper(nums[middle+1:])
            current.left = left_subtree
            current.right = right_subtree

            return current
    
  
        return create_bst_helper(nums)
        