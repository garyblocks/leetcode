# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        dummy.next = head
        prev,end = dummy,dummy
        i = 0
        while i<m-1:
            prev = prev.next
            i+=1
        cur = prev.next
        end = cur.next
        while i<n-1:
            temp = end.next
            end.next = cur
            cur = end
            end = temp
            i+=1
        start = prev.next
        prev.next = cur    
        start.next = end    
        return dummy.next
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """