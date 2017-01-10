# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        if head==None:
            return []
        r = head
        while head.next!=None:
            if head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        return r
        """
        :type head: ListNode
        :rtype: ListNode
        """