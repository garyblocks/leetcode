# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        prev,fast,slow = head,head,head
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev,slow = slow,prev
        if prev: 
            tar = prev.next
        else:
            return
        while tar:
            prev.next = tar.next
            tar.next = slow.next
            slow.next = tar
            tar = prev.next
        while slow != head:
            t1,t2 = head.next,slow.next.next
            head.next = slow.next
            head.next.next = t1
            head = t1
            slow.next = t2
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """