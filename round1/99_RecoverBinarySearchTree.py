# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find(self,node,n,r):
        if not node:
            return
        self.find(node.left,n,r)
        if r[0].val>node.val:
            if not n:
                n.append(r[0])
                n.append(node)
            else:
                n[1]=node
        r[0] = node
        self.find(node.right,n,r)
        
    def recoverTree(self, root):
        n = []
        r = TreeNode(-100000)
        self.find(root,n,[r])
        n[0].val,n[1].val=n[1].val,n[0].val
        return
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """