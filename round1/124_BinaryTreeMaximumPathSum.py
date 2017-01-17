# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self,root,m):
        r1,r2=-1000,-1000
        if root.left:
            r1 = self.find(root.left,m)
        if root.right:
            r2 = self.find(root.right,m)
        m[0] = max(r1,r2,r1+r2+root.val,r1+root.val,r2+root.val,root.val,m[0])
        return max(r1+root.val,r2+root.val,root.val)
    def maxPathSum(self, root):
        m = [-1000]
        if not root:
            return 0
        else:
            self.find(root,m)
        return m[0]
        """
        :type root: TreeNode
        :rtype: int
        """