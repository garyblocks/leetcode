class Solution(object):
    def addBinary(self, a, b):
        i,j = len(a)-1,len(b)-1
        r = ''
        k = 0
        if i>j:
            b = '0'*(i-j)+b
            l = i
        else:
            a = '0'*(j-i)+a
            l = j
        while l>=0:
            t = int(a[l])+int(b[l])+k
            k = t/2
            r = str(t%2) + r
            l-=1
        if k==1:
            r = '1'+r
        return r
        """
        :type a: str
        :type b: str
        :rtype: str
        """