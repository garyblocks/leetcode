# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def rightSideView(self, root):
        line = [root,1]
        r = []
        while len(line)>1:
            t = line.pop(0)
            if not t:
                continue
            if t == 1:
                r.append(v)
                line.append(1)
            else:
                v = t.val
                line.append(t.left)
                line.append(t.right)
        return r
        """
        :type root: TreeNode
        :rtype: List[int]
        """