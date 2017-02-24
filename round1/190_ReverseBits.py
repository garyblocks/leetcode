class Solution(object):
    def reverseBits(self, n):
        s = bin(n)[2:]
        sz = len(s)
        l = list(s)
        l.reverse()
        t = ['0' for i in range(32-sz)]
        rs = ''.join(l+t)
        r = int(rs, 2)
        return r
        """
        :type n: int
        :rtype: int
        """