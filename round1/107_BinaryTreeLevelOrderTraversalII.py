# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trav(self,root,r,l):
        if root and l==len(r):
            r.append([])
        if root:
            r[l].append(root.val)
            self.trav(root.left,r,l+1)
            self.trav(root.right,r,l+1)
    def levelOrderBottom(self, root):
        r = []
        level = 0
        self.trav(root,r,level)
        r.reverse()
        return r
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """