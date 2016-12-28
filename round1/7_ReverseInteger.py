class Solution(object):
    def reverse(self, x):
        if x<0:
            sign = -1
        else:
            sign = 1
        a = sign*x
        l = list(str(a)); l.reverse()
        out = int(''.join(l))
        if out>=2147483651:
            return 0
        return out*sign