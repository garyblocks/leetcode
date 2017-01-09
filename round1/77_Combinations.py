class Solution(object):
    def help(self,s,n,k,r,l):
        if k==0:
            r.append(l[:])
        elif n-s<k:
            return
        else:
            for i in range(s,n):
                l.append(i)
                self.help(i+1,n,k-1,r,l)
                l.remove(i)
    def combine(self, n, k):
        r = []
        self.help(1,n+1,k,r,[])
        return r
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """