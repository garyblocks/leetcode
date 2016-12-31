# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        r = ListNode(0)
        a = r
        while 1:
            if l1==None:
                a.next=l2;
                break
            elif l2==None:
                a.next=l1
                break
            elif l1.val>l2.val:
                while l2.next!=None and l2.next.val==l2.val:
                    a.next=l2; a=a.next; l2=l2.next
                a.next=l2; a=a.next; l2=l2.next
            elif l1.val<l2.val:
                while l1.next!=None and l1.next.val==l1.val:
                    a.next=l1; a=a.next; l1=l1.next
                a.next=l1; a=a.next; l1=l1.next
            else:
                while l2.next!=None and l2.next.val==l2.val:
                    a.next=l2; a=a.next; l2=l2.next
                while l1.next!=None and l1.next.val==l1.val:
                    a.next=l1; a=a.next; l1=l1.next
                a.next=l2; a=a.next; l2=l2.next
                a.next=l1; a=a.next; l1=l1.next
        return r.next
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """