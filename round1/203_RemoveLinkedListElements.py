# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        cur,prev = head,dummy
        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur = cur.next
            else:
                prev = cur
                cur = cur.next
        return dummy.next
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """