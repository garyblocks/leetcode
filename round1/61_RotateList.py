# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return head
        first=head
        a = head
        l=1
        while a.next:
            a=a.next
            l+=1
        k%=l
        if k==0:
            return head
        while k>0:
            first=first.next
            k-=1
        second = head
        while first.next:
            first=first.next
            second=second.next
        first.next=head
        head=second.next
        second.next=None
        return head
        
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """