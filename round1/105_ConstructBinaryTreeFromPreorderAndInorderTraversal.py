# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def build(self,root,pre,x,y,a,b):
        if a:
            lnode = TreeNode(pre[x])
            root.left = lnode
            i = a.index(pre[x])
            self.build(lnode, pre,x+1,x+len(a), a[:i], a[i+1:])
        if b:
            rnode = TreeNode(pre[x+len(a)])
            root.right = rnode
            j = b.index(pre[x+len(a)])
            self.build(rnode, pre,x+len(a)+1,y, b[:j],b[j+1:])
        return
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        else:
            root = TreeNode(preorder[0])
            i = inorder.index(preorder[0])
            self.build(root, preorder,1,len(preorder),inorder[:i],inorder[i+1:])
            return root
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """