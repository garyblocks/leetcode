# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        l1,l2 = 0,0
        t1,t2 = headA,headB
        while t1:
            l1+=1
            t1 = t1.next
        while t2:
            l2+=1
            t2 = t2.next
        t1,t2 = headA,headB
        if l1>l2:
            for i in range(l1-l2):
                t1 = t1.next
        elif l2>l1:
            for i in range(l2-l1):
                t2 = t2.next
        if t1==t2:
            return t1
        elif not t1 or not t2:
            return None
        while True:
            if not t1.next:
                return None
            elif not t2.next:
                return None
            elif t1.next==t2.next:
                return t1.next
            else:
                t1 = t1.next
                t2 = t2.next
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """