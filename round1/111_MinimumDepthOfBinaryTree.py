# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def minDepth(self, root):
        queue = [False,root]  
        length = 0
        if not root:
            return 0
        while queue:
            t = queue.pop(0)
            if t == False:
                length+=1
                queue.append(False)
                continue
            if not t:
                continue
            elif not t.left and not t.right:
                return length
            else:
                queue.append(t.left)
                queue.append(t.right)
            
        """
        :type root: TreeNode
        :rtype: int
        """