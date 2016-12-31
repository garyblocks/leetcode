class Solution(object):
    def divide(self, dividend, divisor):
        a = abs(divisor); b = abs(dividend); r = 0
        if a == 0:
            return MAX_INT
        elif dividend==divisor:
            return 1
        elif dividend+divisor==0:
            return -1
        if a>b:
            return 0
        c = a;d = 1;a = 0
        while c>=divisor:
            if a < b:
                c,d = c << 1, d<<1
                a += c
                r += d
            if a == b:
                break
            if a > b:
                a -= c; r-=d
                c,d = c >> 1, d>>1
                a += c; r += d
        if (divisor<0 and dividend>0) or (divisor>0 and dividend<0):
            r = -r
        if r > 2147483647:
            r = 2147483647
        if r < -2147483648:
            r = -2147483648
        return r
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """