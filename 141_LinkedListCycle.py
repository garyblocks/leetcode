# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        while head.next!=head:
            if not head.next:
                return False
            t=head.next
            head.next=head.next.next
            t.next=head
        return True
        
        """
        :type head: ListNode
        :rtype: bool
        """