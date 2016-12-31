# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        if head==None or head.next==None:
            return head
        a,b = head, head.next
        a.next = b.next
        b.next = a
        head = b
        while a.next!=None and a.next.next!=None:
            b = a.next.next
            a.next.next = b.next
            b.next = a.next
            a.next = b
            a = a.next.next
        return head
        
        """
        :type head: ListNode
        :rtype: ListNode
        """