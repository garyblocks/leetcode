# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addone(self,s,lists,r,a):
        if len(s)==0:
            return r.next
        a.next = lists[s[0]]
        a = a.next
        while lists[s[0]].next == None:
            s = s[1:]
            if len(s)==0:
                return r.next
            a.next = lists[s[0]]
            a = a.next
        else:
            lists[s[0]] = lists[s[0]].next
            i = 0
            while i+1<len(s) and lists[s[i+1]].val<lists[s[i]].val:
                s[i+1],s[i] = s[i], s[i+1]
                i+=1
        return self.addone(s,lists,r,a)
        
    def mergeKLists(self, lists):
        if lists==[]:
            return []
        k = len(lists)
        d = {}
        r = ListNode(0)
        a = r
        for i in range(k):
            if lists[i]==None:
                continue
            else:
                d.update({i:lists[i].val})
        s = sorted(d,key=d.get)
        return self.addone(s,lists,r,a)
            
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """