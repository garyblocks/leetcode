# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def depth(self,root):
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif root.left and root.right:
            return 1+max(self.depth(root.left),self.depth(root.right))
        elif root.left:
            return 1+self.depth(root.left)
        else:
            return 1+self.depth(root.right)
            
    def maxDepth(self, root):
        return self.depth(root)
        """
        :type root: TreeNode
        :rtype: int
        """