class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        a = int('1'+'0'*(len(bin(m))-2),2)
        if a<n:
            return 0
        else:
            r = m
            for i in range(m+1,n+1):
                r&=i
            return r
        """
        :type m: int
        :type n: int
        :rtype: int
        """