class Solution(object):
    def convertToTitle(self, n):
        r = ''
        start = ord('A')
        while n>0:
            t=n%26
            n=int(n/26)
            if t==0:
                r='Z'+r
                n-=1
            else:
                r=chr(t-1+start)+r
        return r
        """
        :type n: int
        :rtype: str
        """