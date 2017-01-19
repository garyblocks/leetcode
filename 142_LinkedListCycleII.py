# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        fast,slow = head,head
        cnt = 0
        while fast and fast.next:
            cnt+=1
            fast,slow = fast.next.next,slow.next
            if fast == slow:
                break
        if fast == slow and cnt>0:
            check = head
            while cnt>0:
                check=check.next
                cnt-=1
            while check != head:
                check = check.next
                head = head.next
            return check
        else:
            return None
        """
        :type head: ListNode
        :rtype: ListNode
        """