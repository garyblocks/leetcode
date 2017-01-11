# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def check(self,p,q):
        if p.val!=q.val:
            return False
        if p.left and p.right:
            if q.left and q.right:
                return self.check(p.left,q.left) and self.check(p.right,q.right)
            else:
                return False
        elif p.left==None and p.right==None:
            return p.left==q.left and p.right==q.right
        elif p.left==None:
            if q.left==None and q.right:
                return self.check(p.right,q.right)
            else:
                return False
        else:
            if q.right==None and q.left:
                return self.check(p.left,q.left)
            else:
                return False
    def isSameTree(self, p, q):
        if p and q:
            return self.check(p,q)
        elif not p and not q:
            return True
        else:
            return False
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """