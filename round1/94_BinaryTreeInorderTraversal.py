# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self,root):
        old = root
        prev = root
        if not root:
            return
        while root.left:
            prev = root
            root = root.left
        if root.right:
            if root == old:
                old = root.right
            else:
                prev.left = root.right
            return root.val,old
        else:
            if root==old:
                return root.val,None
            prev.left = None
            return root.val,old
    def inorderTraversal(self, root):
        r=[]
        while root:
            val,root = self.find(root)
            r.append(val)
        return r
        """
        :type root: TreeNode
        :rtype: List[int]
        """