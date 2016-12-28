# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a,b=l1,l2
        m,n=1,1
        num1,num2=l1.val,l2.val
        while a.next != None:
            m*=10
            a = a.next
            num1=num1+a.val*m
        while b.next != None:
            n*=10
            b = b.next
            num2=num2+b.val*n
        num=str(num1+num2)
        num=num[::-1]
        a=ListNode(num[0])
        c=a
        for i in range(len(num)-1):
            c.val=int(num[i])
            c.next=ListNode(int(num[i+1]))
            c=c.next
        return a    
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
