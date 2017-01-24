# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        def lsort(a,b):
            while a.next != b and a.val==a.next.val:
                a = a.next
            if a.next == b or a.next.next == b:
                return
            tar, cur = a.next, a.next.next
            prev = tar
            while cur!=b:
                if cur.val < tar.val:
                    prev.next = cur.next
                    t = a.next
                    a.next = cur
                    cur.next = t
                    cur = prev.next
                else:
                    cur = cur.next
                    prev = prev.next
            lsort(a,tar)
            lsort(tar,b)
        dummy = ListNode(0)
        dummy.next = head
        lsort(dummy,None)
        return dummy.next
        """
        :type head: ListNode
        :rtype: ListNode
        """