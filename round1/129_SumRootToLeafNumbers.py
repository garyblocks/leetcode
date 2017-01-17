# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self,root,total,part):
        if not root:
            return
        if not root.left and not root.right:
            total[0]+=(part*10+root.val)
        else:
            self.find(root.right,total,part*10+root.val)
            self.find(root.left,total,part*10+root.val)
        return
    def sumNumbers(self, root):
        total = [0]
        part = 0
        self.find(root,total,part)
        return total[0]
        """
        :type root: TreeNode
        :rtype: int
        """