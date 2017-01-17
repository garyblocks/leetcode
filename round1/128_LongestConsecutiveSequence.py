class Solution(object):
    def longestConsecutive(self, nums):
        def count(cur,n,s):
            a,b=cur,cur
            while a+1 in s:
                s.remove(a+1)
                a+=1
                n+=1
            while b-1 in s:
                s.remove(b-1)
                b-=1
                n+=1
            return n
        s = set(nums)
        max = 0
        while s:
            cur,n= s.pop(),1
            n = count(cur,n,s)
            if n>max:
                max = n
        return max
        """
        :type nums: List[int]
        :rtype: int
        """