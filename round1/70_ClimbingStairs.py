class Solution(object):
    def fact(self,m):
        if m!=0:
            return m*self.fact(m-1)
        else:
            return 1 
    def climbStairs(self, n):
        r = 0
        for i in range(n/2+1):
            r += self.fact((n-i*2)+i)/(self.fact(i)*self.fact(n-i*2))
        return r
        """
        :type n: int
        :rtype: int
        """