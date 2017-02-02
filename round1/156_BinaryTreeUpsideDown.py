# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def upsideDownBinaryTree(self, root):
        final = root
        def help(root,prev,right):
            if root.left:
                final = help(root.left,root,root.right)
            else:
                final = root
            cur = root
            cur.left = right
            cur.right = prev
            return final
        if root:
            return help(root, None, None)
        return final
        """
        :type root: TreeNode
        :rtype: TreeNode
        """