# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        stack = [root]
        while stack:
            temp = []
            for i in range(len(stack)):
                if not stack[i]:
                    continue
                if stack[i].left:
                    temp.append(stack[i].left)
                if stack[i].right:
                    temp.append(stack[i].right)
                if i+1<len(stack):
                    stack[i].next=stack[i+1]
            stack = temp