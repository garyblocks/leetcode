# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def valid(self,root):
        r = [True,root.val,root.val]
        if root.left:
            left = self.valid(root.left)
            r[1] = left[1]
            r[0] = r[0] and left[0]
            if left[2]>=root.val:
                r[0]=False
        if root.right:
            right = self.valid(root.right)
            r[2] = right[2]
            r[0] = r[0] and right[0]
            if right[1]<=root.val:
                r[0]=False
        return r
    def isValidBST(self, root):
        if not root:
            return True
        else:
            return self.valid(root)[0]
        """
        :type root: TreeNode
        :rtype: bool
        """