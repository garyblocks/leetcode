class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        n,d = abs(numerator),abs(denominator)
        r = ""
        t,q,cnt = {},-1,0
        flag = True
        while n:
            q = int(n/d)
            r = r + str(q)
            if n%d in t:
                r = r[:t[n%d]] + "("+r[t[n%d]:]+")"
                break
            if flag and n%d:
                r = r + '.'
                flag = False
                cnt+=len(r)-1
            cnt +=1
            t[n%d]=cnt
            n = n%d*10
        if numerator*denominator<0:
            r = "-"+r
        return "0" if not r else r
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """