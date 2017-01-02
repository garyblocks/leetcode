class Solution(object):
    def next(self,r):
        i = 0; s=''; cnt=1
        while i<len(r):
            if i<len(r)-1 and r[i+1]!=r[i]:
                s+=str(cnt)
                s+=r[i]
                cnt=1
                i+=1
            elif i==len(r)-1:
                s+=str(cnt)
                s+=r[i]
                i+=1
            else:
                cnt+=1
                i+=1
        return s
                
    def countAndSay(self, n):
        r = '1'
        for i in range(n-1):
            r = self.next(r)
        return r
            
        """
        :type n: int
        :rtype: str
        “””
