class Solution(object):
    def count(self,n,dp):
        r = 0
        if dp[n]>0:
            return dp[n]
        else:
            for i in range(n):
                r += self.count(i,dp)*self.count(n-i-1,dp)
            dp[n]=r
        return r
    def numTrees(self, n):
        dp = [1,1,2]+[-1 for i in range(n)]
        r = self.count(n,dp)
        return r
            
        """
        :type n: int
        :rtype: int
        """