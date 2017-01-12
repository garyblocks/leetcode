# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def update(self,root,flag):
        if not flag:
            return 0,flag
        if root==None:
            return 0,True
        h1,flag1=self.update(root.left,flag)
        h2,flag2=self.update(root.right,flag)
        flag = flag1 and flag2 and (h1-h2)*(h1-h2)<=1
        h = max(h1,h2)+1
        return h,flag
    def isBalanced(self, root):
        flag=True
        height,flag=self.update(root,flag)
        return flag
        """
        :type root: TreeNode
        :rtype: bool
        """