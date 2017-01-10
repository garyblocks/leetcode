# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteDuplicates(self, head):
        root = ListNode(-1)
        root.next = head
        slow,fast = root,head
        while fast:
            if fast.next and fast.next.val==fast.val:
                fast=fast.next
            else:
                if fast==slow.next:
                    fast=fast.next
                    slow=slow.next
                else:
                    slow.next=fast.next
                    fast=fast.next
        return root.next
        """
        :type head: ListNode
        :rtype: ListNode
        """