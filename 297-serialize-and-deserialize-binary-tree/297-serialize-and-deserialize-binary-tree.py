# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        BFS - queue
        """
        # from collections import deque

        # queue = deque([root])
        # result = []

        # while queue:

        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         result.append(node.val)
        #         if node.val != '*':
        #             if node.left:
        #                 queue.append(node.left)
        #             else:
        #                 queue.append(TreeNode('*'))
        #             if node.right:
        #                 queue.append(node.right)
        #             else:
        #                 queue.append(TreeNode('*'))

        # return result
        def serialize_helper(node):
            if node:
                vals.append(str(node.val))
                serialize_helper(node.left)
                serialize_helper(node.right)
            else:
                vals.append('#')
        vals = []
        serialize_helper(root)
        return ' '.join(vals)

               

    def deserialize(self, data):
        """Decodes your encoded data to a tree.

        :type data: str
        :rtype: TreeNode
        """
        # if not data:
        #     return None

        # root = TreeNode(data[0])
        # for i in range(1, len(data)):
        #     if data[i] != '*':
        #         if not root.left:
        #             root.left = TreeNode(data[i])
        #         else:
        #             if not root.right:
        #                 root.right = TreeNode(data[i])
        #     node = TreeNode(data[i])



        def deserialize_helper():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = deserialize_helper()
            node.right = deserialize_helper()
            return node
        vals = iter(data.split())
        return deserialize_helper()
