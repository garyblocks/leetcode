class Solution(object):
    def power(self, x, n, extra):
        if n==1:
            return x*extra
        else:
            if n%2==1:
                extra*=x
            n/=2
            x*=x
            return self.power(x,n,extra)
            
    def myPow(self, x, n):
        extra = 1
        if n==0:
            return 1.0
        elif n>0:
            return self.power(x,n,extra)
        elif n<0:
            return 1.0/self.power(x,-n,extra)
        """
        :type x: float
        :type n: int
        :rtype: float
        """