# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def check(self,root,sum):
        if not root:
            return False
        elif not root.left and not root.right and root.val==sum:
            return True
        else:
            return self.check(root.left,sum-root.val) or self.check(root.right,sum-root.val)
    def hasPathSum(self, root, sum):
        return self.check(root,sum)
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """