# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        from collections import deque
        d = deque([root])
        # d.append('d')
        # d.popleft()

        ans = []

        while d:
            k,s=len(d),0
            for i in range(len(d)):
                node = d.popleft()
                s += node.val
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
            ans.append(s/float(k))

        return ans
