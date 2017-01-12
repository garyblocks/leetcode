# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def readlevel(self,stack,r,a):
        newstack = []
        level = []
        while stack:
            temp = stack.pop(0)
            if not temp:
                continue
            else:
                newstack.append(temp.left)
                newstack.append(temp.right)
                level.append(temp.val)
        if level:
            if a:
                level.reverse()
            a=not a
            r.append(level)
            self.readlevel(newstack,r,a)
            
    def zigzagLevelOrder(self, root):
        r = []
        stack = [root]
        self.readlevel(stack,r,False)
        return r
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """