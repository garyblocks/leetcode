class Solution(object):
    def isHappy(self, n):
        s = set()
        s.add(n)
        while True:
            new = 0
            while n>0:
                new+=(n%10)**2
                n = int(n/10)
            if new == 1:
                return True
            elif new in s:
                return False
            else:
                s.add(new)
                n = new
        """
        :type n: int
        :rtype: bool
        """