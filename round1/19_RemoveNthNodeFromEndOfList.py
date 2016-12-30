# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        l = []
        a = head
        if head.next == None:
            return l
        while a.next != None:
            l.append(a)
            a = a.next
        l.append(a)
        if n==len(l):
            head = head.next
        else:
            l[-n-1].next=l[-n].next
        return head
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """