# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.vector = []
        while root:
            self.vector.append(root)
            root = root.left
        """
        :type root: TreeNode
        """
        

    def hasNext(self):
        return self.vector
        """
        :rtype: bool
        """
        

    def next(self):
        cur = self.vector.pop()
        v = cur.val
        cur = cur.right
        while cur:
            self.vector.append(cur)
            cur = cur.left
        return v
        """
        :rtype: int
        """
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())