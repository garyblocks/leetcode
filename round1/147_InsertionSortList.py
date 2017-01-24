# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        def insert(r,n):
            s = r
            if r.val>n.val:
                n.next = r
                return n
            while r.next:
                if r.next.val>n.val:
                    n.next = r.next
                    r.next = n
                    return s
                r = r.next
            r.next = n
            return s
        if not head:
            return None
        else:
            r = ListNode(head.val)
        head = head.next
        while head:
            r = insert(r,ListNode(head.val))
            head = head.next
        return r
        """
        :type head: ListNode
        :rtype: ListNode
        """