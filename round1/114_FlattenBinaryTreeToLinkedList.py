# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        if not root:
            return
        prev = TreeNode(None)
        stack = [root]
        while stack:
            t = stack.pop()
            prev.right = t
            prev.left = None
            if t.right:
                stack.append(t.right)
            if t.left:
                stack.append(t.left)
            prev = t
            
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """