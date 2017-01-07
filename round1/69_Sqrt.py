class Solution(object):
    def mySqrt(self, x):
        a = 1.0
        while abs(a*a-x)>0.5:
            a = 0.5*(a+x/a)
        return int(a)
        """
        :type x: int
        :rtype: int
        “””