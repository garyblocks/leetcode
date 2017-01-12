# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tra(self,r,root,l):
        if not root:
            return
        if l==len(r):
            r.append([])
        r[l].append(root.val)
        self.tra(r,root.left,l+1)
        self.tra(r,root.right,l+1)
    def levelOrder(self, root):
        r = []
        level=0
        self.tra(r,root,level)
        return r
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """