# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        if k==1 or head==[]:
            return head
        dummy = ListNode(0); dummy.next=head
        f,prev = dummy, dummy
        while True:
            cnt = 0
            while cnt < k:
                if f.next==None:
                    return dummy.next
                else:
                    f = f.next; cnt+=1
            f = f.next
            cur = prev.next;  start = prev
            while cur!=f:
                nxt = cur.next
                cur.next = prev
                prev = cur; cur = nxt
            t = start.next
            start.next.next = f; start.next = prev
            f,prev = t,t
            
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """