# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def build(self,root,io,a,b,po):
        if len(po)<=1:
            return
        mid = io.index(root.val)-a
        if mid>0:
            root.right = TreeNode(po[1])
            self.build(root.right,io,a,a+mid,po[1:mid+1])
        if mid+1<len(po):
            root.left = TreeNode(po[mid+1])
            self.build(root.left,io,mid+a+1,b,po[mid+1:])
    def buildTree(self, inorder, postorder):
        if not inorder:
            return None
        inorder.reverse()
        postorder.reverse()
        root = TreeNode(postorder[0])
        self.build(root,inorder,0,len(inorder)-1,postorder)
        return root
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """