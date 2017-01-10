# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        start,tail = ListNode(0),ListNode(0)
        r1,r2 = start,tail
        cur = head
        while cur:
            if cur.val<x:
                start.next = cur
                start = start.next
            else:
                tail.next = cur
                tail = tail.next
            cur = cur.next
        start.next = r2.next
        tail.next = None
        return r1.next
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """