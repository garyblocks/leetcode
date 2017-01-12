# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def check(self,a,b):
        if not a and not b:
            return True
        elif a and b:
            if a.val!=b.val:
                return False
            else:
                return (self.check(a.left,b.right) and self.check(a.right,b.left))
        else:
            return False
    def isSymmetric(self, root):
        if root:
            return self.check(root.left,root.right)
        else:
            return True
        """
        :type root: TreeNode
        :rtype: bool
        """