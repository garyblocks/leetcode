class Solution(object):
    def romanToInt(self, s):
        o = 0; step = 1;
        r1 = ['I','II','III','IV','V','VI','VII','VIII','IX']
        r2 = ['X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        r3 = ['C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        r4 = ['M','MM','MMM']
        r = [r4,r3,r2,r1]
        for i in r:
            o *= 10
            for j in range(len(i)-1,-1,-1):
                if i[j] in s:
                    if s == s.lstrip(i[j]):
                        continue
                    o += j+1
                    s = s.lstrip(i[j])
                    print(o,s)
        return(o)
        """
        :type s: str
        :rtype: int
        """