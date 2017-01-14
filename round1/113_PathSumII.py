# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self,root,sum,r,t):
        if not root:
            return
        else:
            t.append(root.val)
            if sum-root.val==0 and not root.left and not root.right:
                r.append(t[:])
            else:
                self.find(root.left,sum-root.val,r,t)
                self.find(root.right,sum-root.val,r,t)
            t.pop()
        
    def pathSum(self, root, sum):
        r,t = [],[]
        self.find(root,sum,r,t)
        return r
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """