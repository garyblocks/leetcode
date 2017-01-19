# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution(object):
    def copyRandomList(self, head):
        nodes = {}
        r = RandomListNode(0)
        new = r
        i = head
        l1,l2 = [],[]
        while head:
            if head in nodes:
                temp = nodes[head]
            else:
                temp = RandomListNode(head.label)
                nodes[head] = temp
            if head.random:
                if head.random in nodes:
                    temp.random = nodes[head.random]
                else:
                    tempRand = RandomListNode(head.random.label)
                    nodes[head.random] = tempRand
                    temp.random = tempRand
            new.next = temp
            head = head.next; new = new.next
        return r.next
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """