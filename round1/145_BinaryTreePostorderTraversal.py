# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        r = []
        def traverse(root):
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            r.append(root.val)
        if root:
            traverse(root)
        return r
        """
        :type root: TreeNode
        :rtype: List[int]
        """