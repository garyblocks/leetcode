import math
class Solution(object):
    def perm(self,n):
        r = 1
        while n>0:
            r*=n
            n-=1
        return r
    def getPermutation(self, n, k):
        r=""
        vec = [self.perm(i) for i in range(1,n+1)]
        vec.reverse()
        num = [str(i) for i in range(1,n+1)]
        for i in range(1,len(vec)):
            t=math.ceil(float(k)/vec[i])
            if t>=1:
                print t
                r+=num.pop(int(t)-1)
                if k%vec[i]==0 and k>=vec[i]:
                    k=vec[i]
                else:
                    k%=vec[i]
        r+=''.join(num)
        return r
        """
        :type n: int
        :type k: int
        :rtype: str
        """