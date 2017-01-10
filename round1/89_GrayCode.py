class Solution(object):
    def change(self,r,i,s,n):
        if i>0:
            self.change(r,i-1,s,n)
            if s[n-i]==0:
                s[n-i]=1
            else:
                s[n-i]=0
            t = 0
            for k in range(n):
                t += 2**(n-k-1)*s[k]
            r.append(t)
            self.change(r,i-1,s,n)
    def grayCode(self, n):
        r = [0]
        s = []
        for i in range(n):
            s.append(0)
        self.change(r,n,s,n)
        return r
        """
        :type n: int
        :rtype: List[int]
        """