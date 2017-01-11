# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def gen(self,ls,res,se):
        tree = TreeNode(ls[0])
        cur = tree
        for i in ls[1:]:
            while cur:
                prev = cur
                if i>cur.val:
                    if cur.left:
                        return
                    if not cur.right:
                        cur.right=TreeNode(i)
                        break
                    cur = cur.right
                else:
                    if not cur.left:
                        cur.left=TreeNode(i)
                        break
                    cur = cur.left
            cur = tree
        res.append(tree)
    def add(self,nums,l,r):
        if len(nums)==0:
            r.append(l)
            return 
        for i in range(len(nums)):
            new = nums[:i]+nums[i+1:]
            ln = l[:]
            ln.append(nums[i])
            self.add(new,ln,r)
    def generateTrees(self, n):
        if n==0:
            return []
        r,l = [],[]
        nums = [i+1 for i in range(n)]
        self.add(nums,l,r)
        res,se = [],set()
        for i in r:
            self.gen(i,res,se)
        return res
        """
        :type n: int
        :rtype: List[TreeNode]
        """