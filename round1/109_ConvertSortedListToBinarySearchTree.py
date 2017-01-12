# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def build(self,nums):
        if not nums:
            return None
        else:
            mid = (len(nums)-1)/2
            root = TreeNode(nums[mid])
            root.left = self.build(nums[:mid])
            root.right = self.build(nums[mid+1:])
            return root
    def sortedListToBST(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return self.build(nums)
        """
        :type head: ListNode
        :rtype: TreeNode
        """