# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        stack,r = [root],[]
        while stack:
            temp = stack.pop()
            r.append(temp.val)
            if temp.right:
                stack.append(temp.right)
            if temp.left:
                stack.append(temp.left)
        return r
        """
        :type root: TreeNode
        :rtype: List[int]
        """