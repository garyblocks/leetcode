class Solution(object):
    def trailingZeroes(self, n):
        res = 0
        while n>=5:
            n = int(n/5)
            res+=n
        return res
        """
        :type n: int
        :rtype: int
        """